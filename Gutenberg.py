#! /usr/bin/python


import argparse
import subprocess

def start():
    pars = argparse.ArgumentParser(description='A tool to find books/resources for academic purposes')
    pars.add_argument('-d', '--delete', nargs='*', default='blacklist.txt', help='-d [site1] [site2]...')
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
                print(1) 
            elif getattr(args, ftype) and ftype == 'videos':
                print(2) 
            elif getattr(args, ftype) and ftype == 'jpg':
                print(3)
            elif getattr(args, ftype) and ftype == 'png':
                print(4)
            elif getattr(args, ftype) and ftype == 'zip':
                print(5)
            elif getattr(args, ftype) and ftype == 'mp3':
                print(6)
            elif getattr(args, ftype) and ftype == 'mp4':
                print(7)
            elif getattr(args, ftype) and ftype == 'ppt':
                print(8)
            elif getattr(args, ftype) and ftype == 'word':
                print(9)
            else:
                print(10)

            


    
if __name__ == '__main__':
    start()


