import asyncpg
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import POSTGRES_URL, bot
import buttons

from handlers import commands, start
from handlers.FSM import review_client
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from handlers.FSM.order import order_FSM_start


# =======================================================================================================================
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


async def all_products(message: types.Message):
    await message.answer(f"Выберите город:\n\n"
                         f"Для перехода в главное меню нажмите на кнопку /start",
                         reply_markup=buttons.city_markup)

async def all_products_bishkek(message: types.Message):
    await message.answer(f"Выберите категорию товара:\n\n"
                         f"Для перехода в главное меню нажмите на кнопку /start",
                         reply_markup=buttons.all_categories_bishkek)

async def all_products_osh(message: types.Message):
    await message.answer(f"Выберите категорию товара:\n\n"
                         f"Для перехода в главное меню нажмите на кнопку /start",
                         reply_markup=buttons.all_categories_osh)

async def all_products_moscow(message: types.Message):
    await message.answer(f"Выберите категорию товара:\n\n"
                         f"Для перехода в главное меню нажмите на кнопку /start",
                         reply_markup=buttons.all_categories_moscow)


"""Вывод категорий"""


async def load_category(message: types.Message, city: str, category: str):

    pool = await asyncpg.create_pool(POSTGRES_URL)  # Инициализируем переменную conn перед try

    categories = await get_product_from_category(pool, category, city)

    if not categories:
        if city == "Бишкек":
            await message.answer(f"Категория '{category}' в городе '{city}' не найдена.\n\n"
                                 f"Для выхода в главное меню нажмите на кнопку /start",
                                 reply_markup=buttons.all_categories_bishkek)
            return
        elif city == "Ош":
            await message.answer(f"Категория '{category}' в городе '{city}' не найдена.\n\n"
                                 f"Для выхода в главное меню нажмите на кнопку /start",
                                 reply_markup=buttons.all_categories_osh)
        else:
            await message.answer(f"Категория '{category}' в городе '{city}' не найдена.\n\n"
                                 f"Для выхода в главное меню нажмите на кнопку /start",
                                 reply_markup=buttons.all_categories_moscow)
    else:
        for category in categories:
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


        if city == "Бишкек":
            await message.answer(f"Это все товары из категории - {category[6]}",
                                 reply_markup=buttons.all_categories_bishkek)
        elif city == "Ош":
            await message.answer(f"Это все товары из категории - {category[6]}",
                                 reply_markup=buttons.all_categories_osh)
        else:
            await message.answer(f"Это все товары из категории - {category[6]}",
                                 reply_markup=buttons.all_categories_moscow)

async def all_products_bishkek_obuv(message: types.Message):
    await load_category(message, city="Бишкек", category="Обувь")

async def all_products_bishkek_nijnee(message: types.Message):
    await load_category(message, city="Бишкек", category="Нижнее_белье")

async def all_products_bishkek_accesuary(message: types.Message):
    await load_category(message, city="Бишкек", category="Акссесуары")

async def all_products_bishkek_verhniya(message: types.Message):
    await load_category(message, city="Бишкек", category="Верхняя_одежда")

async def all_products_bishkek_shtany(message: types.Message):
    await load_category(message, city="Бишкек", category="Штаны")


async def all_products_osh_obuv(message: types.Message):
    await load_category(message, city="Ош", category="Обувь")


async def all_products_osh_nijnee(message: types.Message):
    await load_category(message, city="Ош", category="Нижнее_белье")


async def all_products_osh_accesuary(message: types.Message):
    await load_category(message, city="Ош", category="Акссесуары")


async def all_products_osh_verhniya(message: types.Message):
    await load_category(message, city="Ош", category="Верхняя_одежда")


async def all_products_osh_shtany(message: types.Message):
    await load_category(message, city="Ош", category="Штаны")


async def all_products_moscow_obuv(message: types.Message):
    await load_category(message, city="Москва", category="Обувь")


async def all_products_moscow_nijnee(message: types.Message):
    await load_category(message, city="Москва", category="Нижнее_белье")


async def all_products_moscow_accesuary(message: types.Message):
    await load_category(message, city="Москва", category="Акссесуары")


async def all_products_moscow_verhniya(message: types.Message):
    await load_category(message, city="Москва", category="Верхняя_одежда")


async def all_products_moscow_shtany(message: types.Message):
    await load_category(message, city="Москва", category="Штаны")



# =======================================================================================================================
def register_all_products(dp: Dispatcher):
    dp.register_message_handler(all_products, commands=["Товары!"])
    dp.register_message_handler(all_products_bishkek, Text(equals="Бишкек"))
    dp.register_message_handler(all_products_osh, Text(equals="Ош"))
    dp.register_message_handler(all_products_moscow, Text(equals="Москва"))

    dp.register_message_handler(all_products_bishkek_obuv, Text(equals="Обувь_Бишкек"))
    dp.register_message_handler(all_products_bishkek_nijnee, Text(equals="Нижнее_белье_Бишкек"))
    dp.register_message_handler(all_products_bishkek_verhniya, Text(equals="Верхняя_одежда_Бишкек"))
    dp.register_message_handler(all_products_bishkek_shtany, Text(equals="Штаны_Бишкек"))
    dp.register_message_handler(all_products_bishkek_accesuary, Text(equals="Акссесуары_Бишкек"))

    dp.register_message_handler(all_products_osh_obuv, Text(equals="Обувь_Ош"))
    dp.register_message_handler(all_products_osh_nijnee, Text(equals="Нижнее_белье_Ош"))
    dp.register_message_handler(all_products_osh_verhniya, Text(equals="Верхняя_одежда_Ош"))
    dp.register_message_handler(all_products_osh_shtany, Text(equals="Штаны_Ош"))
    dp.register_message_handler(all_products_osh_accesuary, Text(equals="Акссесуары_Ош"))

    dp.register_message_handler(all_products_moscow_obuv, Text(equals="Обувь_Москва"))
    dp.register_message_handler(all_products_moscow_nijnee, Text(equals="Нижнее_белье_Москва"))
    dp.register_message_handler(all_products_moscow_verhniya, Text(equals="Верхняя_одежда_Москва"))
    dp.register_message_handler(all_products_moscow_shtany, Text(equals="Штаны_Москва"))
    dp.register_message_handler(all_products_moscow_accesuary, Text(equals="Акссесуары_Москва"))