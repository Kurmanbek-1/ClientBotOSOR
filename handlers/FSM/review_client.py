from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import buttons
from datetime import datetime


# =======================================================================================================================


class review_fsm(StatesGroup):
    articule = State()
    name = State()
    review = State()
    city = State()
    submit_photo = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    await review_fsm.articule.set()
    await message.answer("Артикуль товара?", reply_markup=buttons.cancel_markup)


async def load_articule(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["articule"] = message.text
    await review_fsm.next()
    await message.answer("Название товара!?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await review_fsm.next()
    await message.answer("Отзыв о товаре!?\n" "?/5")


async def load_review(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["review"] = message.text
    await review_fsm.next()
    await message.answer("Филиал!?", reply_markup=buttons.city_markup)


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["city"] = message.text
    await review_fsm.next()
    await message.answer("Вы хотите отправить фото товара?", reply_markup=buttons.yesno)


async def submit_photo(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await review_fsm.next
        await message.answer("Отправьте фотку товара")
    elif message.text == 'Нет':
        async with state.proxy() as data:
            data["date"] = datetime.now()
            await message.answer(f"Артикуль товара: {data['articule']}"
                                 f"Название товара: {data['name']}\n"
                                 f"Отзыв о товаре: {data['review']}\n"
                                 f"Город: {data['city']}", )
        await review_fsm.submit.set()
        await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id
        data["date"] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f"Данные товара: \n"
                    f"Артикуль товара: {data['articule']}"
                    f"Название товара: {data['name']}\n"
                    f"Отзыв о товаре: {data['review']}\n"
                    f"Город: {data['city']}",
        )
    await review_fsm.next()
    await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == "да":
            if data['city'] == 'Бишкек':
                # Запись в базу данных!
                pass

            elif data['city'] == 'ОШ':
                # Запись в базу данных!
                pass

            elif data['city'] == 'Москва 1-филиал':
                # Запись в базу данных!
                pass

            elif data['city'] == 'Москва 2-филиал':
                # Запись в базу данных!
                pass

            await message.answer('Готово!', reply_markup=buttons.start)
            await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.start)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start)


# =======================================================================================================================


def register_review(dp: Dispatcher):
    dp.register_message_handler(
        cancel_reg, Text(equals="Отмена", ignore_case=True), state="*"
    )
    dp.register_message_handler(fsm_start, commands=["Написать_отзыв"])

    dp.register_message_handler(load_articule, state=review_fsm.articule)
    dp.register_message_handler(load_name, state=review_fsm.name)
    dp.register_message_handler(load_review, state=review_fsm.review)
    dp.register_message_handler(load_city, state=review_fsm.city)

    dp.register_message_handler(submit_photo, state=review_fsm.submit_photo)
    dp.register_message_handler(load_photo, state=review_fsm.photo, content_types=["photo"])

    dp.register_message_handler(load_submit, state=review_fsm.submit)
