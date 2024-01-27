from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()


TOKEN = config('TOKEN')
Director = [1738805992, ]
CHANNEL_ID = int(config('CHANNEL_ID'))
Admins = [995712956, 908379438, ]

Manager = [995712956, 908379438, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

# ip = config('ip')
# PostgresUser = config('PostgresUser')
# PostgresPassword = config('PostgresPassword')
# DATABASE = config('DATABASE')

user = config("POSTGRES_USER")
password = config("POSTGRES_PASSWORD")
hostname = config("POSTGRES_HOST")
database_name = config("POSTGRES_DB")
port = config("POSTGRES_PORT")

POSTGRES_URL = f"postgresql://{user}:{password}@{hostname}:{port}/{database_name}"

data_b = Database(POSTGRES_URL)