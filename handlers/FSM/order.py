from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

import buttons
from config import bot, Manager

from handlers import commands, start
from handlers.FSM import review_client


# ======================================================================================================================
class OrderFSM(StatesGroup):
    full_name = State()
    contact = State()
    size = State()
    submit = State()


async def order_FSM_start(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['articule'] = call.data.replace("to_order", "").strip()
    await call.message.answer("Ваше ФИО ?!", reply_markup=buttons.cancel_markup)
    await OrderFSM.full_name.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["full_name"] = message.text
    await message.answer("Нажми на кнопку, чтобы поделиться своим контактом.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [types.KeyboardButton(text="Отправить контакт", request_contact=True)],
                             ],
                             resize_keyboard=True
                         ))
    await OrderFSM.next()


async def load_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.contact
        await message.answer('Введите размер!', reply_markup=buttons.cancel_markup)
    await OrderFSM.next()



async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.answer(f"Данные о товаре:\n"
                         f"Размер: {data['size']}\n"
                         f"Артикул товара: {data['articule']}"
                         f"Ваше ФИО: {data['full_name']}")
    await message.answer("Всё правильно?", reply_markup=buttons.submit_markup)
    await OrderFSM.next()


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for i in Manager:
            if message.text.lower() == 'да':
                await state.finish()
                await message.answer('Отлично!\n'
                                     'Ваш заказ принят! ✅\n'
                                     'Пожалуйста ожидайте с вами свяжутся наши менеджеры ⏳', reply_markup=buttons.start)

                await bot.send_message(chat_id=i, text=f"📢Новый заказ!!!\n"
                                                       f"ФИО: {data['full_name']}\n"
                                                       f"Атикул: {data['articule']}\n"
                                                       f"Размер: {data['size']}\n"
                                                       f"\n\n"
                                                       f"Снизу контакты клиента ⬇️")
                await bot.send_contact(chat_id=i,
                                       phone_number=data['contact']['phone_number'],
                                       first_name=data['contact']['first_name'])

            else:
                await message.answer("Отмена!")
                await state.finish()

    # Вывод из базы


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Заказ отменён!', reply_markup=buttons.start)


async def about_command_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await commands.about(message)


async def start_command_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await start.start_command(message)


async def review_command_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await review_client.fsm_start(message)


def register_order(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='/cancel', ignore_case=True), state='*')
    dp.register_message_handler(about_command_fsm, Text(equals="/about", ignore_case=True), state="*")
    dp.register_message_handler(start_command_fsm, Text(equals="/start", ignore_case=True), state="*")
    dp.register_message_handler(review_command_fsm, Text(equals="/review", ignore_case=True), state="*")
    dp.register_callback_query_handler(order_FSM_start,
                                       lambda call: call.data and call.data.startswith("to_order"))
    dp.register_message_handler(load_fullname, state=OrderFSM.full_name)
    dp.register_message_handler(load_contact, state=OrderFSM.contact, content_types=['contact'])
    dp.register_message_handler(load_size, state=OrderFSM.size)
    dp.register_message_handler(load_submit, state=OrderFSM.submit)
