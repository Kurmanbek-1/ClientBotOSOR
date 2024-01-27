import asyncpg
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, CHANNEL_ID
import os
from keyboards import buttons
from config import user, password, database_name, hostname
# Добавим константу для количества товаров, выводимых изначально
PRODUCTS_PER_PAGE = 7

# Добавим словарь для отслеживания счетчиков для каждого чата
chat_counters = {}


async def get_conn():
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database_name, host=hostname)
    return conn


async def all_products(message: types.Message, state: FSMContext):
    category_name = message.text
    data = await state.get_data()
    city = data.get("city")

    try:
        conn = await get_conn()
        # Используем счетчик для ограничения количества отображаемых товаров
        counter = chat_counters.get(message.chat.id, 0)
        products = await conn.fetch("SELECT * FROM products_coming OFFSET $1 LIMIT $2", counter, PRODUCTS_PER_PAGE)
    except Exception as e:
        await message.answer(f"Ошибка SQL-запроса: {e}")
        return
    finally:
        await conn.close()

    for product in products:
        photo_path = product[9]

        if not os.path.exists(photo_path):
            print(f"Файл не найден: {photo_path}")
            continue
        try:
            with open(photo_path, 'rb') as photo:
                await message.answer_photo(photo=photo, caption=f"Товар: {product[1]}\n"
                                                                f"Информация о товаре: {product[2]}\n"
                                                                f"Цена: {product[4]}\n"
                                                                f"Город: {product[5]}\n"
                                                                f"Категория: {product[6]}\n"
                                                                f"Артикул: {product[7]}\n",
                                           reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"В канал! {product[0]}",
                                                                                                        callback_data=f"Разослать {product[0]}")))
        except Exception as e:
            print(f"Ошибка при открытии файла {photo_path}: {e}")
            continue

    chat_counters[message.chat.id] = counter + PRODUCTS_PER_PAGE


    if len(products) == PRODUCTS_PER_PAGE:
        await message.answer("Хотите посмотреть остальные товары ❓:", reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("Да!✅", callback_data="load_more")
        ))


async def complete_send_products(call: types.CallbackQuery):
    product_id = call.data.replace("Разослать ", "")

    try:
        conn = await get_conn()
        products = await conn.fetch(f"SELECT * FROM products_coming WHERE id = {product_id}")
    except Exception as e:
        print(f"Ошибка SQL-запроса: {e}")
        return
    finally:
        await conn.close()

    if not products:
        print(f"Товар с ID {product_id} не найден.")
        return

    for product in products:
        photo_path = product[9]

        if photo_path is None:
            print("Отсутствует путь к изображению для продукта.")
            continue

        if not os.path.exists(photo_path):
            print(f"Файл не найден: {photo_path}")
            continue

        try:
            with open(photo_path, 'rb') as photo:
                sent_message = await bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=f"Товар: {product[1]}\n"
                                                                                             f"Информация о товаре: {product[2]}\n"
                                                                                             f"Цена: {product[4]}\n"
                                                                                             f"Город: {product[5]}\n"
                                                                                             f"Категория: {product[6]}\n"
                                                                                             f"Артикул: {product[7]}\n",
                                                    reply_markup=buttons.startForAdmins)
        except Exception as e:
            print(f"Ошибка при открытии файла {photo_path}: {e}")
            continue


    await call.answer(text="Отправлено! ✅", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)



async def load_more_products(call: types.CallbackQuery, state: FSMContext):
    # Получаем текущее значение счетчика из состояния
    data = await state.get_data()
    counter = data.get("counter", 0)

    # Увеличиваем счетчик на PRODUCTS_PER_PAGE
    counter += PRODUCTS_PER_PAGE

    # Сохраняем новое значение счетчика в состояние
    await state.update_data(counter=counter)

    # Получаем товары для отображения
    await all_products(call.message, state)

    # Добавим отладочные сообщения
    print(f"Текущий счетчик: {counter}")
    print(f"Отправленное сообщение: {call.message.text}")





def register_button_all_products(dp: Dispatcher):
    dp.register_message_handler(all_products, commands=['Готовые_товары!'])
    dp.register_callback_query_handler(complete_send_products,
                                       lambda call: call.data and call.data.startswith("Разослать "))
    dp.register_callback_query_handler(load_more_products, text="load_more")
