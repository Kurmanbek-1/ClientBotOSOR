from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()

TOKEN = "6300075993:AAHYw2L4LJ8BgoVwx1P1nO3kHPjWzivHxBM"
Director = [6451475162, ]
CHANNEL_ID = int(config('CHANNEL_ID'))
Admins = [995712956, ]

Manager = [995712956, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

POSTGRES_URL = "postgresql://postgres:123@postgres_compass:5432/osor_tg_bot"
data_b = Database(POSTGRES_URL)
