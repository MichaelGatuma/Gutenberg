#!/usr/bin/env python
import requests
import urllib
from bs4 import BeautifulSoup

def url_scrape(soup):
    for item in soup.find_all('h3', attrs={'class' : 'r'}):
        try:
            links.append(item.a['href'].split('/url?q=')[1].split('&sa', 1)[0])
        except TypeError:
            pass

def paginate(soup):
    for page in soup.find_all('table', attrs={'id' : 'nav'}):
        for number in page.find_all('a'):
            if (number['href'].split('start=')[1].split('&sa')[0]) not in pages and len(pages) == 0:
                pages.append(number['href'].split('start=')[1].split('&sa')[0])
            elif (number['href'].split('start=')[1].split('&sa')[0]) not in pages and (number['href'].split('start=')[1].split('&sa')[0]) > pages[0]:
                pages.append(number['href'].split('start=')[1].split('&sa')[0])

def make_query(increment, term):
    r = requests.get('https://www.google.com/search?q={}&start={}'.format(query, increment))
    soup = BeautifulSoup(r.content, 'html.parser')

    url_scrape(soup)
    paginate(soup)


    
query = 'lag'
query = urllib.quote_plus(query)

i = 0

pages = []
links = []
make_query(i, query)

try:
    while i < pages[-1]:
        i = pages.pop(0)
        make_query(i, query)

except ValueError:
    pass



print(pages)
print(links)
