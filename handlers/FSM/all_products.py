from aiogram import types, Dispatcher


# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher.filters.state import State, StatesGroup
#
# from keyboards import buttons
# from datetime import datetime
#
#
# # =======================================================================================================================
#
#
# class review_fsm(StatesGroup):
#     category = State()
#     category_price = State()
#     city = State()
#
#
# async def fsm_start(message: types.Message):
#     await review_fsm.category.set()
#     await message.answer("Категория товара?", reply_markup=buttons.cancel_markup)
#
#
# async def load_category(message: types.Message):
#     if message.text == 'Обувь':
#         await message.answer('')
#         await review_fsm.next()
#
#         await message.answer("Ценовая категория товара?")
#
#     elif message.text == 'Нижнее_белье':
#         await message.answer('')
#         await review_fsm.next()
#         await message.answer("Ценовая категория товара?")
#
#     elif message.text == 'Акссесуары':
#         await message.answer('')
#         await review_fsm.next()
#         await message.answer("Ценовая категория товара?")
#
#     elif message.text == 'Верхняя_одежда':
#         await message.answer('')
#         await review_fsm.next()
#         await message.answer("Ценовая категория товара?")
#
#     elif message.text == 'Штаны':
#         await message.answer('')
#         await review_fsm.next()
#         await message.answer("Ценовая категория товара?")
#
#     else:
#         await message.answer("Нет такой категории!\n"
#                              "Снизу есть кнопки категорий, пользуйтесь ими")
#
#
#
# async def load_category_price(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["category_price"] = message.text
#     await review_fsm.next()
#     await message.answer("Филиал?")
#
#
# async def load_city(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["city"] = message.text
#     await state.finish()
#
#
# async def cancel_reg(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is not None:
#         await state.finish()
#         await message.answer('Отменено!', reply_markup=buttons.start)


# =======================================================================================================================
async def test(message: types.Message):
    await message.answer('Здесь будут все товары!')


def register_all_products(dp: Dispatcher):
    dp.register_message_handler(test, commands=['Товары'])

    # dp.register_message_handler(
    #     cancel_reg, Text(equals="Отмена", ignore_case=True), state="*"
    # )
    # dp.register_message_handler(fsm_start, commands=["Товары"])
    #
    # dp.register_message_handler(load_articule, state=review_fsm.articule)
    # dp.register_message_handler(load_name, state=review_fsm.name)
    # dp.register_message_handler(load_review, state=review_fsm.review)
    # dp.register_message_handler(load_city, state=review_fsm.city)
