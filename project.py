import sqlite3
import requests
from bs4 import BeautifulSoup as bs
class Table:
    connection = sqlite3.connect('pr.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,
                                        name VARCHAR(100) UNIQUE NOT NULL,
                                        link VARCHAR(100) NOT NULL);""")
    connection = sqlite3.connect('pr.db')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO user (name, link) 
                      VALUES('weather', 'https://ua.sinoptik.ua/?utm_source=ukr.net&utm_medium=main_page&utm_campaign=main_izbrannoe'), 
                      ('value', 'https://www.oschadbank.ua/currency-rate'),
                      ('news','https://www.ukr.net')""")
    connection = sqlite3.connect('pr.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT name FROM user""")
    data = cursor.fetchall()
    print(data)
    connection.commit()
    connection.close()
class Reaq:
    r = requests.get("https://www.oschadbank.ua/currency-rate")
    html = bs(r.text, "html.parser")
    data1 = html.find_all('span', class_='heading-block-currency-rate__table-txt body-regular')
    cur = []
    for i in data1:
        print(i.text)
class Reaq1:
    r = requests.get("https://ua.sinoptik.ua/?utm_source=ukr.net&utm_medium=main_page&utm_campaign=main_izbrannoe")
    html = bs(r.text, "html.parser")
    data2 = html.find_all('tr', class_='tempreture')
    cur = []
    for i in data2:
        print(i.text)
class Reaq:
    r = requests.get("https://www.ukr.net")
    html = bs(r.text, "html.parser")
    data1 = html.find_all('ul', class_='feed__section--top')
    cur = []
    for i in data1:
        print(i.text)