#!/usr/bin/python3.6
import requests
import urllib
from bs4 import BeautifulSoup

def url_scrape(soup, link, blist):
    for item in soup.find_all('h3', attrs={'class' : 'r'}):
        try:
            if blist:
                ignore_l = False
                ignore = open('blacklist.txt', 'r')
                for i in ignore:
                    i = i.replace('\n', '')
                    if i in (item.a['href'].split('/url?q=')[1].split('&sa', 1)[0]) and i != '':
                        ignore_l = True
                if not ignore_l:
                    link.append(item.a['href'].split('/url?q=')[1].split('&sa', 1)[0])
            else:
                link.append(item.a['href'].split('/url?q=')[1].split('&sa', 1)[0])
        except TypeError:
            pass
        except IndexError:
            link.append(item.a['href'])
        except FileNotFoundError:
            ignore = open('blacklist.txt', 'w+')
            ignore.close()

def paginate(soup, pg):
    for page in soup.find_all('table', attrs={'id' : 'nav'}):
        for number in page.find_all('a'):
            if int(number['href'].split('start=')[1].split('&sa')[0]) not in pg and len(pg) == 0:
                pg.append(int(number['href'].split('start=')[1].split('&sa')[0]))
            elif int(number['href'].split('start=')[1].split('&sa')[0]) not in pg and int(number['href'].split('start=')[1].split('&sa')[0]) > pg[0]:
                pg.append(int(number['href'].split('start=')[1].split('&sa')[0]))

def make_query(increment, term, filet, p, l, blacklist, s_pattern):
    if filet == 'file types' and s_pattern == 'search patterns':
        r = requests.get('https://www.google.com/search?q={}&start={}'.format(term, increment))
    elif filet != 'file types' and s_pattern == 'search patterns':
        r = requests.get('https://www.google.com/search?q={} {}&start={}'.format(term, filet, increment)) 
    elif filet == 'file types' and s_pattern != 'search patterns':
        r = requests.get('https://www.google.com/search?q={}{}&start={}'.format(s_pattern, term, increment))
    else:
        r = requests.get('https://www.google.com/search?q={}{} {}&start={}'.format(s_pattern, term, filet, increment))

    soup = BeautifulSoup(r.content, 'html.parser')
    url_scrape(soup, l, blacklist)
    paginate(soup, p)

def search(query, filetype, blacklists, search_pattern):
    i = 0
    if filetype != 'file types':
        filetype = 'filetype:' + filetype
    pages, links = [], []
    make_query(i, query, filetype, pages, links, blacklists, search_pattern)
    try:
        while i < pages[-1]:
            i = pages.pop(0)
            make_query(i, query, filetype, pages, links, blacklists, search_pattern)
    except ValueError:
        pass
    return(links)
