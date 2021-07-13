import logging

from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
