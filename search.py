#!/usr/bin/env python
import requests
import urllib
from bs4 import BeautifulSoup

def url_scrape():
    for item in soup.find_all('h3', attrs={'class' : 'r'}):
        try:
            print(item.a['href'].split('/url?q=')[1].split('&sa', 1)[0])
        except TypeError:
            pass

def paginate():
    for page in soup.find_all('table', attrs={'id' : 'nav'}):
        for number in page.find_all('a'):
            if (number['href'].split('start=')[1].split('&sa')[0]) not in pages:
                pages.append(number['href'].split('start=')[1].split('&sa')[0])

query = 'lag'
query = urllib.quote_plus(query)

r = requests.get('https://www.google.com/search?q={}'.format(query))
soup = BeautifulSoup(r.content, 'html.parser')

i = 0

pages = []
paginate()
print(pages)

links = []
url_scrape()
