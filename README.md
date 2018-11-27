# Gutenberg
A tool to find books/resources for academic purposes and discards sites such as chegg, coursehero, etc.

## Gui vs Terminal
Gutenberg comes as either a command-line tool or as a GUI, with their own set of dependencies. 

## Dependencies (GUI)
The required Python libraries are as follows: sys, PyQt5, requests, urllib and bs4. Sys and Urllib come with an up to date python3, as for the others they can be installed with these commands:
```bash
$ pip3 install bs4
$ pip3 install requests
$ sudo apt-get install python3-pyqt5
```
## Dependencies (Terminal)
The required Python libraries are the following: argparse, subprocess, requests, bs4 and urllib. Most are automatically installed by keeping your Python version up to date. As for bs4 and requests just use the following command from the terminal:
```bash
$ pip3 install bs4
$ pip3 install requests
```
## Running Gutenberg 
You will need to make Gutenberg.py executable.

## Running Gutenberg (Terminal Only)
To search pdf:
```bash
$ ./Gutenberg.py -p [query] 
```
To search jpg:
```bash
$ ./Gutenberg.py -j [query] 
```
To search png:
```bash
$ ./Gutenberg.py -pg [query] 
```
To search zip:
```bash
$ ./Gutenberg.py -z [query] 
```
To search mp3:
```bash
$ ./Gutenberg.py -m3 [query] 
```
To search mp4:
```bash
$ ./Gutenberg.py -m4 [query] 
```
To search powerpoint:
```bash
$ ./Gutenberg.py -pp [query] 
```
To search word file:
```bash
$ ./Gutenberg.py -w [query] 
```
