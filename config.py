from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

storage = MemoryStorage()

TOKEN = "6664323534:AAGINBs1rzRZ3wsyTjE1YFKUrcbGb57FLfQ"
CHANNEL_ID = int(config('CHANNEL_ID'))


Director = [659106628, 995712956]

Admins = [659106628, ]

Developers = [995712956, ]


Manager = [659106628, ]

# TOKEN = "6947024020:AAFJZzy-QRY6l2-rKNkUzYGh-JYMB7fnEWc"
# CHANNEL_ID = int(config('CHANNEL_ID'))
#
#
# Director = [6451475162, 1738805992]
#
# Admins = [995712956, 1000541805, 958938518, 6127093234, ]
#
# Developers = [995712956, ]
#
#
# Manager = [659106628, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

POSTGRES_URL = "postgresql://postgres:123@localhost:5432/osor_tg_bot"
data_b = Database(POSTGRES_URL)


