from bs4 import BeautifulSoup
import urllib
import requests
import random

def user_agent():
    user_agents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36']
    word = "Антигриппин"
    url_new  = "https://omsk.uteka.ru/search/?query=Антигриппин"
    HEADER = {'User-Agent': random.choice(user_agents)}
    page = requests.get(url_new, data=HEADER)
    return page

def parse():
    connect = user_agent()
    filtered = {}
    if connect.status_code == 200:
        soup = BeautifulSoup(connect.text, "html.parser")
        all = soup.findAll('div', class_= "product-preview ui-panel ui-panel_size_s ui-panel_clickable")
        for data in all:
            names = data.find('span', {'itemprop': 'name'}).text
            buy = data.find('div', {'class': 'ui-price__content'}).text
            if(buy != 'NoneType'):
                print(buy)