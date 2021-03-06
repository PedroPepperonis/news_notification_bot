import os


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

DATABASE_URL = os.getenv('DATABASE_URL')

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))

URL_STOPGAME = 'https://stopgame.ru'
URL_IGROMANIA = 'https://www.igromania.ru'
URL_VGTIMES = 'https://vgtimes.ru/tags/%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8'
