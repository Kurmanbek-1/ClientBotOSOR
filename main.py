from aiogram.utils import executor
import logging
from handlers.FSM import review_client, send_to_tg_channel, all_products, \
    ButtoninProducts, order, reservation, tryon
# ===========================================================================
from config import dp, bot, Developers
from handlers.commands import register_start
from handlers import start
import buttons
from config import data_b
from db import db_orm

from aiogram import types

# ==================================================================================================================
async def on_startup(_):
    for Admin in Developers:
        await bot.send_message(chat_id=Admin, text="Бот запущен!", reply_markup=buttons.startForAdmins)
        await db_orm.sql_create()
        await data_b.connect()


# ==================================================================================================================
start.register_start(dp)
db_orm.sql_get_ORM(dp)
review_client.register_review(dp)
send_to_tg_channel.register_send_to_channel(dp)

all_products.register_all_products(dp)
ButtoninProducts.register_button_all_products(dp)
tryon.register_try_on(dp)

reservation.register_reservation(dp)
order.register_order(dp)
register_start(dp)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Такой команды нет ❌\n'
                         'Нажмите на /start и у вас выйдут все ваши кнопки!')

# ===========================================================================
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

