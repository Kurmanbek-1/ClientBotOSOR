from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()

TOKEN = "6947024020:AAFJZzy-QRY6l2-rKNkUzYGh-JYMB7fnEWc"
Director = [659106628, ]
CHANNEL_ID = int(config('CHANNEL_ID'))
Admins = [659106628, ]

Developers = [995712956, 659106628, ]

Manager = [659106628, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

POSTGRES_URL = "postgresql://postgres:123@postgres_compass:5432/osor_tg_bot"
data_b = Database(POSTGRES_URL)
