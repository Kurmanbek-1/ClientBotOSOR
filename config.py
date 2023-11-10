from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN = config('TOKEN')
Director = [1738805992, ]
CHANNEL_ID = int(config('CHANNEL_ID'))

Admins = [995712956, 908379438, ]


bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)
