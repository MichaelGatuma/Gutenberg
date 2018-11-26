#!/usr/bin/env python
import requests
import urllib
from bs4 import BeautifulSoup

def url_scrape(links):
    for item in soup.find_all('h3', attrs={'class' : 'r'}):
        links.append(item.a['href'].split('&sa')[0].split('/url?q=')[1])

def paginate(pages):
    for page in soup.find_all('table', attrs={'id' : 'nav'}):
        for number in page.find_all('a'):
            if (number['href'].split('start=')[1].split('&sa')[0]) not in pages:
                pages.append(number['href'].split('start=')[1].split('&sa')[0])

query = 'wajdnawdliwunilnuid'
query = urllib.quote_plus(query)

r = requests.get('https://www.google.com/search?q={}'.format(query))
soup = BeautifulSoup(r.content, "html.parser")

i = 0

pages = []
paginate(pages)

links = []
url_scrape(links)

try:
    while i < pages[-1]:
        

except IndexError:
    pass

