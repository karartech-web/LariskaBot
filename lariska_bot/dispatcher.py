import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# جرب هذه الطريقة التي ستجبر الكود على أخذ القيمة أو التوقف بخطأ واضح إذا كانت فارغة
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("لم يتم العثور على المتغير TOKEN! تأكد من إضافته في إعدادات Railway.")
print(f"DEBUG: The token value is: {TOKEN}")
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
