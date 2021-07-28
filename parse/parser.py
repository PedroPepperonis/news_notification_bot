import requests
from bs4 import BeautifulSoup as bs

from config.config import URL_STOPGAME, URL_IGROMANIA, URL_VGTIMES, HEADERS


def check_last_article(url):
    with open('last_url.txt', 'r') as f:
        urls = f.read().splitlines()
        if url in urls:
            return False
    with open('last_url.txt', 'w') as f:
        for i in urls:
            f.write(i + '\n')
        f.write(url)
        return True


def get_photo_from_igromania(url):
    response = requests.get(url, headers=HEADERS)
    soup = bs(response.content, 'html.parser')
    items = soup.find('div', class_='main_pic_container')
    img_url = items.find('img').get('src')

    return img_url


# stopgame
def get_last_news_from_stopgame():
    response = requests.get(URL_STOPGAME, headers=HEADERS)
    soup = bs(response.content, 'html.parser')
    items = soup.find('section', class_='swiper-wrapper')

    title = items.find('a', class_='img').get('title') + '\n\nИсточник: https://stopgame.ru'
    url = URL_STOPGAME + items.find('a', class_='img').get('href')
    img = items.find('img').get('src')

    data = {'title': title, 'url': url, 'img': img}

    if check_last_article(url):
        return data


# игромания
def get_last_news_from_igromania():
    response = requests.get(URL_IGROMANIA, headers=HEADERS)
    soup = bs(response.content, 'html.parser')
    items = soup.find('div', class_='ac3')

    title = items.find('div', class_='text_block_in').get_text() + '\n\nИсточник: https://www.igromania.ru/'
    url = URL_IGROMANIA + items.find('a', class_='outer_link2').get('href')
    img = get_photo_from_igromania(url)

    data = {'title': title, 'url': url, 'img': img}

    if check_last_article(url):
        return data


# vgtimes
def get_last_news_from_vgtimes():
    main_url = 'https://vgtimes.ru'

    response = requests.get(URL_VGTIMES)
    soup = bs(response.content, 'html.parser')
    items = soup.find('div', class_='item-main')

    title = items.find('span').get_text() + '\n\nИсточник: https://vgtimes.ru/'
    url = items.find('a').get('href')
    img_url = items.find('a', class_='image')
    img = main_url + img_url.find('img').get('data-src')

    data = {'title': title, 'url': url, 'img': img}

    if check_last_article(url):
        return data
