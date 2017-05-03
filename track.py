import simplejson as json
import os
from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError

url_list = []
price_list = []
try:
	fr = open("price-track.txt")
except IOError:
	print("Error while opening the file")

## Extracting url and prices from the text file
for line in fr:
    if(line != '\n'):
        json_data = json.loads(line)
        url_list.append(json_data['url'])
        price_list.append(json_data['price'])

fr.close()
## Fetch the url and check the price

for url, price in zip(url_list,price_list):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url,headers=headers)
    doc = html.fromstring(page.content)
    XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
    XPATH_NAME = '//h1[@id="title"]//text()'
    RAW_NAME = doc.xpath(XPATH_NAME)
    RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
    SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
    NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
    if(float(SALE_PRICE[1:]) < float(price)):
        print("notify the user that the price for ", NAME , " has dropped")
    

