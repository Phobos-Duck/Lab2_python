from bs4 import BeautifulSoup
import requests
import random
import bot_main

def user_agent(word):
    user_agents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36']
    url_new = f"https://omsk.uteka.ru/search/?query={word}"
    HEADER = {'User-Agent': random.choice(user_agents)}
    page = requests.get(url_new, data=HEADER)
    return page

def parse(word):
    connect = user_agent(word)
    if connect.status_code == 200:
        soup = BeautifulSoup(connect.text, "html.parser")
        all_image = soup.findAll('div', class_="product-preview__header")
        all_medicines = soup.findAll('div', class_="product-preview ui-panel ui-panel_size_s ui-panel_clickable")
        for data2 in all_image:
            try:
                image = data2.find('img', {'class': '"ui-lazy-image"'}).get("src")
                bot_main.img(image)
            except AttributeError:
                return False

        for data in all_medicines:
            try:
                names = data.find('span', {'itemprop': 'name'}).text
                buy = data.find('div', {'class': 'ui-price__content'}).text
                bot_main.filter(names, buy)
            except AttributeError:
                return False







