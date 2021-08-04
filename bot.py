import asyncio

# from aiogram.utils.executor import start_webhook
from aiogram.utils.executor import start_polling

import handlers
from handlers.users.send_news import bot_send
from loader import dp, bot
# from config.config import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dispatcher):
    return


async def on_shutdown(dispatcher):
    return


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.create_task(bot_send(10))
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(bot_send(10))
    start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
