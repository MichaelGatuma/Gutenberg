#!/usr/bin/env python
import requests
import urllib
from bs4 import BeautifulSoup

class Search:
    def __init__(self, query, file_type):
        self.query = query
        self.file_type = file_type
        self.query = urllib.quote_plus(self.query)

    def url_scrape(soup, link):
        for item in soup.find_all('h3', attrs={'class' : 'r'}):
            try:
                link.append(item.a['href'].split('/url?q=')[1].split('&sa', 1)[0])
            except TypeError:
                pass

    def paginate(soup, pg):
        for page in soup.find_all('table', attrs={'id' : 'nav'}):
            for number in page.find_all('a'):
                if (number['href'].split('start=')[1].split('&sa')[0]) not in pg and len(pages) == 0:
                    pg.append(number['href'].split('start=')[1].split('&sa')[0])
                elif (number['href'].split('start=')[1].split('&sa')[0]) not in pg and (number['href'].split('start=')[1].split('&sa')[0]) > pg[0]:
                    pg.append(number['href'].split('start=')[1].split('&sa')[0])

    def make_query(increment, term, p, l):
        r = requests.get('https://www.google.com/search?q={}&start={}'.format(query, increment))
        soup = BeautifulSoup(r.content, 'html.parser')

        url_scrape(soup, l)
        paginate(soup, p)

    def search():
        i = 0
        pages, links = [], []
        make_query(i, query, pages, links)
        try:
            while i < pages[-1]:
                i = pages.pop(0)
                make_query(i, query, pages, links)
        except ValueError:
            pass
