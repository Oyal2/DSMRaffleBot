__author__ = 'Oyal2'
from random import getrandbits
import requests
import time

def cook(amt):
     for i in range(1, amt + 1):
        url = 'http://london.doverstreetmarket.com/nike/01.html';
        s = requests.session()
        email = 'emial+{}@gmail.com'.format(getrandbits(40));
        payload = {
            'entry_2017578399': '',#Full Name
            'entry_1814423206': email,
            'entry_798857510': '',#Zip Code
            'entry_1299443671': '',#City
            'entry_1247748047': 'Air Jordan 1', #<-- Shoe Model
            'entry_287029075': '',#Phone Number
            'entry_199279768': 'Size US 11.5',#<-- SHOE SIZE
        }
        proxies = {
          'http':'35.190.59.82:8080',#'http': 'http://10.10.1.10:3128', format should be like this
          'http': '198.199.91.220:3128',#'http': 'socks5://user:pass@host:port',
        }
        
        s.post(url, data=payload, proxies=proxies);
        print('Created {}/{} Entries'.format(i,amt))
        time.sleep(2)


amt = input('How many entries?  ')
cook(int(amt))
