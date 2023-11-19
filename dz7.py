import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://ua.sinoptik.ua/?utm_source=ukr.net&utm_medium=main_page&utm_campaign=main_izbrannoe")
html = bs(r.text, "html.parser")
data = html.find_all('tr', class_='tempreture')
data2 = html.find_all('div', class_='main loaded')
cur = []
for i in data:
    print(i.td.text)
# for i in data2:
#     print(i.p.text)