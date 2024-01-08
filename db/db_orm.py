import sqlite3
from aiogram import types, Dispatcher
from config import Admins, bot
from db import sql_queris

db = sqlite3.connect("db/review.db")
cursor = db.cursor()


async def sql_create():
    if db:
        print("База Client подключена!")
    cursor.execute(sql_queris.CREATE_TABLE_REVIEW)
    db.commit()


async def sql_insert_review(state):
    async with state.proxy() as data:
        cursor.execute(sql_queris.INSERT_INTO_TABLE_REVIEW, tuple(data.values()))
        db.commit()


async def get_all_reviews(message: types.Message):
    reviews = cursor.execute(sql_queris.SELECT_CHECKS_REVIEWS).fetchall()

    columns = [column[0] for column in cursor.description]

    for review in reviews:
        if message.from_user.id in Admins:
            review_dict = dict(zip(columns, review))

            if review_dict["photo"]:
                photo = review_dict["photo"]
            else:
                photo = open("media/img.png", "rb")

            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=f"Данные товара: \n"
                        f"Артикуль товара: {review_dict['articule']}\n"
                        f"Название товара: {review_dict['name']}\n"
                        f"Отзыв о товаре: {review_dict['info']}\n"
                        f"Город: {review_dict['city']}",
            )


def sql_get_ORM(dp: Dispatcher):
    dp.register_message_handler(get_all_reviews, commands=['Все_отзывы!'])
