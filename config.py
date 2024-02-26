from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database


Director = [6451475162, 1738805992, ]
Admins = [995712956, 1000541805, 958938518, 6127093234, ]
Manager = [659106628, 995712956, ]
Developers = [995712956, ]


TOKEN = '7022495453:AAHseOVVzCl5mDSrfKQivn9y55iKxIMntpU'

# TOKEN = config('TOKEN')
CHANNEL_ID = int(config('CHANNEL_ID'))
bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


ip = config('ip')
PostgresUser = config('PostgresUser')
PostgresPassword = config('PostgresPassword')
DATABASE = config('DATABASE')

POSTGRES_URL = f"postgresql://{PostgresUser}:{PostgresPassword}@{ip}/{DATABASE}"
data_b = Database(POSTGRES_URL)
