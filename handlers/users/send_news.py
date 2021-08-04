import asyncio

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import bot
from parse.parser import get_last_news_from_stopgame, get_last_news_from_igromania, get_last_news_from_vgtimes


async def bot_send(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        print('Прошло 10 секунд')
        stopgame_data = get_last_news_from_stopgame()
        igromania_data = get_last_news_from_igromania()
        vgtimes_data = get_last_news_from_vgtimes()
        print('Данные с сайтов получены')
        if stopgame_data:
            btn = InlineKeyboardButton('Читать', url=stopgame_data['url'])
            kb = InlineKeyboardMarkup().add(btn)
            await bot.send_photo(628447199, photo=stopgame_data['img'], caption=stopgame_data['title'], reply_markup=kb)
            print('данные с стопгейм отпрвлены или нет')

        if igromania_data:
            btn = InlineKeyboardButton('Читать', url=igromania_data['url'])
            kb = InlineKeyboardMarkup().add(btn)
            await bot.send_photo(628447199, photo=igromania_data['img'], caption=igromania_data['title'], reply_markup=kb)
            print('данные с игромании отпрвлены или нет')

        if vgtimes_data:
            btn = InlineKeyboardButton('Читать', url=vgtimes_data['url'])
            kb = InlineKeyboardMarkup().add(btn)
            await bot.send_photo(628447199, photo=vgtimes_data['img'], caption=vgtimes_data['title'], reply_markup=kb)
            print('данные с вгтимес отпрвлены или нет')
