from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot
from keyboards import buttons

import sqlite3

conn = sqlite3.connect('../WorkBot/db/db_bish/Bishkek_db')
cursor = conn.cursor()


# =======================================================================================================================


class all_products_fsm(StatesGroup):
    category = State()


async def fsm_start(message: types.Message):
    await all_products_fsm.category.set()
    await message.answer("Категория товара?", reply_markup=buttons.all_categories)



"""Вывод категорий"""

async def load_category(message: types.Message):
    category_name = message.text

    try:
        cursor.execute("SELECT * FROM products_coming WHERE category = ?", (category_name,))
        categories = cursor.fetchall()
        print(categories)
    except Exception as e:
        await message.answer(f"Произошла ошибка при выполнении SQL-запроса: {e}")
        return


    if not categories:
        await message.answer(f"Категория '{category_name}' не найдена.")
        return
    else:
        for category in categories:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=category[9])


"""----------------"""


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start)


# =======================================================================================================================
def register_all_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="Отмена", ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=["Товары_Бишкек!"])
    dp.register_message_handler(load_category, state=all_products_fsm.category)
