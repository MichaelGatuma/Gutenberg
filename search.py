#!/usr/bin/python3.6
import requests
import urllib
from bs4 import BeautifulSoup

def url_scrape(soup, link):
    for item in soup.find_all('h3', attrs={'class' : 'r'}):
        try:
            link.append(item.a['href'].split('/url?q=')[1].split('&sa', 1)[0])
        except TypeError:
            pass
        except IndexError:
            link.append(item.a['href'])
            
def paginate(soup, pg):
    for page in soup.find_all('table', attrs={'id' : 'nav'}):
        for number in page.find_all('a'):
            if (number['href'].split('start=')[1].split('&sa')[0]) not in pg and len(pg) == 0:
                pg.append(int(number['href'].split('start=')[1].split('&sa')[0]))
            elif (number['href'].split('start=')[1].split('&sa')[0]) not in pg and (number['href'].split('start=')[1].split('&sa')[0]) > pg[0]:
                pg.append(int(number['href'].split('start=')[1].split('&sa')[0]))

def make_query(increment, term, tp, p, l):
    r = requests.get('https://www.google.com/search?q={}{}&start={}'.format(tp, term, increment))
    soup = BeautifulSoup(r.content, 'html.parser')

    url_scrape(soup, l)
    paginate(soup, p)

def search(query, filetype):
    i = 0
    filetype = filetype + ':'
    pages, links = [], []
    make_query(i, query, filetype, pages, links)
    try:
        while i < pages[-1]:
            i = pages.pop(0)
            make_query(i, query, filetype, pages, links)
    except ValueError:
        pass
    return(links)
