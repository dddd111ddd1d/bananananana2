import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.ua/d/uk/obyavlenie/prodam-banan-kievskiy-super-karlik-IDC7KUN.html"
data = requests.get(URL).text

soup = BeautifulSoup(data, features=URL)

product_name = soup.find_all("h1", {"class":"css-1soizd2 er34gjf0"})
product_price = soup.find_all("h3", {"class":"css-ddweki er34gjf0"})
product_description = soup.find_all("div", {"class":"css-bgzo2k er34gjf0"})
Similar_ads = soup.find_all("div", {"class":"css-1wbpwse"})
print("Назва продукта -", product_name)
print("Ціна продукта -", product_price)
print("Опис продукта -", product_description)
print("Схожі товари -", Similar_ads)

                  