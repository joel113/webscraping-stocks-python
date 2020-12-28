import requests
import datetime
import time
import sys
from lxml import etree
from bs4 import BeautifulSoup

stock = sys.argv[1]

try:
    r = requests.get("https://onvista.de/aktien/" + stock + ".")
    data = r.text
    soup = BeautifulSoup(data, features="lxml")
    dom = etree.HTML(str(soup))
    stockPrice = dom.xpath("//*[@id=\"ONVISTA\"]/div/div[1]/div[1]/article/ul/li[1]/span[1]/text()")
    print('{')
    print("\"name\": \"{stock}\",".format(stock = stock))
    print("\"price\": {price}".format(price = str(stockPrice[0]).replace(',','.')))
    print('}')
except:
    print("Did not find any data.")
    raise
