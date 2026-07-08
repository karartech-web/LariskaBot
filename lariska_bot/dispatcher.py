import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# قراءة التوكن من متغيرات البيئة التي ضبطتها في Railway
TOKEN = os.getenv("TOKEN") 

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
