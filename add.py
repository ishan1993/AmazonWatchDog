import simplejson as json
import os
from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError

data = {}
try:
    fw = open('price-track.txt' , 'a')
except IOError:
    print("Error while creating the text file")

choice = True
while choice:
    url = raw_input("Enter the product URL :")
    desired_price = raw_input("Enter the desired price : ")
    data['url'] = url
    data['price'] = desired_price
    fw.write('\n')
    json.dump(data,fw)
    inp = raw_input("Do you want to add more prodcuts, say y/n ??")
    if inp == 'y':
        continue
    else:
        choice = False


fw.close()
