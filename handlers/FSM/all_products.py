import asyncpg
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import POSTGRES_URL, bot
import buttons

from handlers import commands, start
from handlers.FSM import review_client
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# =======================================================================================================================

class all_products_fsm(StatesGroup):
    city = State()
    category = State()
    more_tovars = State()


async def fsm_start(message: types.Message):
    await all_products_fsm.city.set()
    await message.answer(f"Выберите город:\n\n"
                         f"Для перехода в главное меню нажмите на кнопку /cancel",
                         reply_markup=buttons.city_markup)


async def choose_city(message: types.Message, state: FSMContext):
    selected_city = message.text
    await state.update_data(city=selected_city)
    await all_products_fsm.category.set()
    await message.answer(f"Категория товара для города {selected_city}?\n\n"
                         f"Для перехода в главное меню нажмите на кнопку /cancel",
                         reply_markup=buttons.all_categories)


"""Вывод категорий"""


async def get_product_from_category(pool, category, city):
    try:
        async with pool.acquire() as connection:
            categories = await connection.fetch(
                """SELECT * FROM products_coming
                WHERE category = $1 AND city = $2""",
                category, city
            )
            return categories
    except Exception as e:
        await bot.send_message(f"Error executing SQL query: {e}")
        return None


async def load_category(message: types.Message, state: FSMContext):
    category_name = message.text
    data = await state.get_data()
    city = data.get("city")
    pool = await asyncpg.create_pool(POSTGRES_URL)

    if message.text.startswith("/"):
        categories = await get_product_from_category(pool, category_name, city)

        if not categories:
            await message.answer(f"Категория '{category_name}' в городе '{city}' не найдена.\n\n"
                                 f"Для перехода в главное меню нажмите на кнопку /cancel",
                                 reply_markup=buttons.all_categories)
            return

        for category in categories:
            if len(categories) <= 5:
                photo_path = category[9]

                keyboard = InlineKeyboardMarkup(row_width=2).add(
                    InlineKeyboardButton(
                        f"Заказать",
                        callback_data=f"to_order{category[7]}"
                    ),
                    InlineKeyboardButton(
                        f"Бронь",
                        callback_data=f"to_reservation{category[7]}"
                    ),
                    InlineKeyboardButton(
                        f"Примерить",
                        callback_data=f"to_try{category[7]}"
                    )
                )

                with open(photo_path, 'rb') as photo:
                    await message.answer_photo(photo=photo, caption=f"Товар: {category[1]}\n"
                                                                    f"Информация о товаре: {category[2]}\n"
                                                                    f"Цена: {category[4]}\n"
                                                                    f"Город: {category[5]}\n"
                                                                    f"Категория: {category[6]}\n"
                                                                    f"Артикул: {category[7]}\n",
                                               reply_markup=keyboard)
                await message.answer(f"Это все товары из категории: {category[6]}",
                                reply_markup=buttons.city_markup)

            else:
                chunks = [categories[i:i + 5] for i in range(0, len(categories), 5)]
                data = await state.get_data()
                current_chunk = data.get("current_chunk", 0)
                current_products = chunks[current_chunk]

                for product in current_products:
                    photo_path = product[9]

                    keyboard = InlineKeyboardMarkup(row_width=2).add(
                        InlineKeyboardButton(
                            f"Заказать",
                            callback_data=f"to_order{product[7]}"
                        ),
                        InlineKeyboardButton(
                            f"Бронь",
                            callback_data=f"to_reservation{product[7]}"
                        ),
                        InlineKeyboardButton(
                            f"Примерить",
                            callback_data=f"to_try{product[7]}"
                        )
                    )

                    with open(photo_path, 'rb') as photo:
                        await message.answer_photo(photo=photo, caption=f"Товар: {product[1]}\n"
                                                                        f"Информация о товаре: {product[2]}\n"
                                                                        f"Цена: {product[4]}\n"
                                                                        f"Город: {product[5]}\n"
                                                                        f"Категория: {product[6]}\n"
                                                                        f"Артикул: {product[7]}\n",
                                                   reply_markup=keyboard)

                await state.update_data(current_chunk=current_chunk + 1)

                if current_chunk < len(chunks) - 1:
                    ShowMore = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
                    ShowMore.add(KeyboardButton(f'Ещё из категории: {category}'))
                    ShowMore.add(KeyboardButton('Отмена'))
                    await message.answer("Показать еще?", reply_markup=ShowMore)
                    await all_products_fsm.next()

    else:
        category = message.text.split()[-1]

        categories = await get_product_from_category(pool, category, city)

        if categories:
            chunks = [categories[i:i + 5] for i in range(0, len(categories), 5)]
            data = await state.get_data()
            current_chunk = data.get("current_chunk", 0)
            current_products = chunks[current_chunk]

            for product in current_products:
                photo_path = product[9]

                keyboard = InlineKeyboardMarkup(row_width=2).add(
                    InlineKeyboardButton(
                        f"Заказать",
                        callback_data=f"to_order{product[7]}"
                    ),
                    InlineKeyboardButton(
                        f"Бронь",
                        callback_data=f"to_reservation{product[7]}"
                    ),
                    InlineKeyboardButton(
                        f"Примерить",
                        callback_data=f"to_try{product[7]}"
                    )
                )

                with open(photo_path, 'rb') as photo:
                    await message.answer_photo(photo=photo, caption=f"Товар: {product[1]}\n"
                                                                    f"Информация о товаре: {product[2]}\n"
                                                                    f"Цена: {product[4]}\n"
                                                                    f"Город: {product[5]}\n"
                                                                    f"Категория: {product[6]}\n"
                                                                    f"Артикул: {product[7]}\n",
                                               reply_markup=keyboard)
            await state.update_data(current_chunk=current_chunk + 1)

            if current_chunk < len(chunks) - 1:
                ShowMore = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
                ShowMore.add(KeyboardButton(f'Ещё из категории: {category}'))
                ShowMore.add(KeyboardButton('Отмена'))
                await message.answer("Показать еще?", reply_markup=ShowMore)
                await all_products_fsm.more_tovars.set()
            else:
                await all_products_fsm.city.set()
                await message.answer(f"Это все товары из категории: {category}",
                                     reply_markup=buttons.city_markup)


async def load_more(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await load_category(message, state)


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start)

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


# =======================================================================================================================
def register_all_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="/cancel", ignore_case=True), state="*")
    dp.register_message_handler(about_command_fsm, Text(equals="/about", ignore_case=True), state="*")
    dp.register_message_handler(start_command_fsm, Text(equals="/start", ignore_case=True), state="*")
    dp.register_message_handler(review_command_fsm, Text(equals="/review", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=["Товары!"])
    dp.register_message_handler(choose_city, state=all_products_fsm.city)
    dp.register_message_handler(load_category, state=all_products_fsm.category)
    for category in ["Обувь", "Нижнее_белье", "Акссесуары", "Верхняя_одежда", "Штаны"]:
        dp.register_message_handler(load_more, Text(equals=f'Ещё из категории: {category}', ignore_case=True),
                                    state=all_products_fsm.more_tovars)