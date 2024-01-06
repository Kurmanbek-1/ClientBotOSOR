from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()


TOKEN = config('TOKEN')
Director = [1738805992, ]
CHANNEL_ID = int(config('CHANNEL_ID'))
Admins = [995712956, ]

Manager = [995712956, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

# ip = config('ip')
# PostgresUser = config('PostgresUser')
# PostgresPassword = config('PostgresPassword')
# DATABASE = config('DATABASE')

POSTGRES_URL = "postgresql://postgres:123@127.0.0.1:5432/osor_tg_bot"
data_b = Database(POSTGRES_URL)