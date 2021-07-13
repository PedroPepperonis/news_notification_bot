from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Дарова, {message.from_user.first_name}')
    await bot.send_message(f'Дарова, {message.from_user.first_name}')
