from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from keyboards import buttons


# ======================================================================================================================
class OrderFSM(StatesGroup):
    articul = State()
    submit = State()


async def order_FSM_start(message: types.Message):
    await OrderFSM.articul.set()
    await message.answer("Введите артикул товара!")


async def load_articul(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["articule"] = message.text
    await OrderFSM.next()


async def load_submit(message: types.Message):
    await message.answer("Данные о товаре")
    # Вывод из базы


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start)


def register_order(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(order_FSM_start, commands=['Заказать'])
    dp.register_message_handler(load_submit, state=OrderFSM.articul)
    dp.register_message_handler(load_submit, state=OrderFSM.submit)
