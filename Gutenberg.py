#! /usr/bin/env python

import argparse
import subprocess
import requests
from bs4 import BeautifulSoup
from search import search

def start():
    pars = argparse.ArgumentParser(description='A tool to find books/resources for academic purposes')
    pars.add_argument('-p', '--pdf', action='store_true', help='-p to find pdf')
    pars.add_argument('-v', '--videos', action='store_true', help='-v to find videos')
    pars.add_argument('-j', '--jpg', action='store_true', help='-j to find jpg file')
    pars.add_argument('-pg', '--png', action='store_true', help='-pg to find png file')
    pars.add_argument('-z', '--zip', action='store_true', help='-z to find zip file')
    pars.add_argument('-m3', '--mp3', action='store_true', help='-m3 to find mp3')
    pars.add_argument('-m4', '--mp4', action='store_true', help='-m4 to find mp4')
    pars.add_argument('-pp', '--ppt', action='store_true', help='-pp to find power points')
    pars.add_argument('-w', '--word', action='store_true', help='-ww to find word documents')
    pars.add_argument('search', nargs='?', help='search term')
    

    args = pars.parse_args()
    
    if not args.search:
        print('usage: python Gutenberg.py -h')
    else:
        for ftype in vars(args): #Currently Placeholder
            if getattr(args, ftype) and ftype == 'pdf':
                urls = search(args.search, ftype)
                pdf_list = open('pdf_urls.txt', 'w+')
                for url in urls:
                    pdf_list.write(url+'\n')
                pdf_list.close()
            elif getattr(args, ftype) and ftype == 'videos':
                urls = search(args.search, ftype)
                video_list = open('video_urls.txt', 'w+')
                for url in urls:
                    video_list.write(url+'\n')
                video_list.close()

            elif getattr(args, ftype) and ftype == 'jpg':
                urls = search(args.search, ftype)
                jpg_list = open('jpg_urls.txt', 'w+')
                for url in urls:
                    jpg_list.write(url+'\n')
                jpg_list.close()

            elif getattr(args, ftype) and ftype == 'png':
                urls = search(args.search, ftype)
                png_list = open('jpg_urls.txt', 'w+')
                for url in urls:
                    png_list.write(url+'\n')
                png_list.close()

            elif getattr(args, ftype) and ftype == 'zip':
                urls = search(args.search, ftype)
                zip_list = open('jpg_urls.txt', 'w+')
                for url in urls:
                    zip_list.write(url+'\n')
                zip_list.close()

            elif getattr(args, ftype) and ftype == 'mp3':
                urls = search(args.search, ftype)
                mp3_list = open('mp3_urls.txt', 'w+')
                for url in urls:
                    mp3_list.write(url+'\n')
                mp3_list.close()

            elif getattr(args, ftype) and ftype == 'mp4':
                urls = search(args.search, ftype)
                mp4_list = open('mp4_urls.txt', 'w+')
                for url in urls:
                    mp4_list.write(url+'\n')
                mp4_list.close()

            elif getattr(args, ftype) and ftype == 'ppt':
                urls = search(args.search, ftype)
                ppt_list = open('ppt_urls.txt', 'w+')
                for url in urls:
                    ppt_list.write(url+'\n')
                ppt_list.close()

            elif getattr(args, ftype) and ftype == 'word':
                urls = search(args.search, ftype)
                word_list = open('word_urls.txt', 'w+')
                for url in urls:
                    word_list.write(url+'\n')
                word_list.close()
                     
    
if __name__ == '__main__':
    start()


