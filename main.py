import requests
from bs4 import BeautifulSoup

URL = "https://rozetka.com.ua/ua/outward_hound_pt67835/p195264728/"
data = requests.get(URL).text

soup = BeautifulSoup()