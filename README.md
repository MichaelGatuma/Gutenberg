# Gutenberg
A tool to find books/resources for academic purposes and discards sites such as chegg, coursehero, etc.

## Dependencies
The required Python libraries are the following: argparse, subprocess, requests, bs4 and urllib. Most are automatically installed by keeping your Python version up to date. As for bs4 and requests just use the following command from the terminal:
```bash
$ pip install bs4, requests
```
## Running Gutenberg
For the moment, Gutenberg is strictly a command line tool. You will need to make Gutenberg.py executable.
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
