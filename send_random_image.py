import requests

from pprint import pprint
from telegram import Bot



bot = Bot(token='5103331195:AAHXEOnA3xkeBvqWEE9d0imWk0TDWQPP0kk')

URL = 'https://api.thecatapi.com/v1/images/search'
chat_id =  1030447067

response = requests.get(URL).json()
random_cat_url = response[0].get('url')

bot.send_photo(chat_id, random_cat_url)
