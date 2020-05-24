#!/usr/bin/env python3

import requests,re,threading
from bs4 import BeautifulSoup
from queue import Queue
from optparse import OptionParser
from os import chdir,path
from core import lefunny,ua,imgflip
q = Queue()

print(r'''
    __  ___     __  ___             
   /  |/  /__  /  |/  /__  ________ 
  / /|_/ / _ \/ /|_/ / _ \/ ___/ _ \
 / /  / /  __/ /  / /  __(__  )  __/
/_/  /_/\___/_/  /_/\___/____/\___/ 

########### Steal Memes :D  ##############
########### By: @knassar702 #############
	''')
# options
optp = OptionParser(add_help_option=False)
optp.add_option("-t","--threads",dest="thr",type='int')
optp.add_option("-f","--file",dest="file")
optp.add_option("-h","--help",dest="help",action='store_true')
optp.add_option("-p","--page",dest="page",type='int')
opts, args = optp.parse_args()
if opts.help:
	print('''
	-h,--help   | Show help message and exit
	-t,--threads   | Max number of concurrent requests for Downloading Memes (default: 10)
	-f,--f         | Saving Memes in This path (--file='Memes_file')
	-p,--page      | number of Memes pages
	-d,--dump	   | Dump Links Without Download
	-D,--Dump      | Dump Links With Download it
		''')
	exit()
if opts.page:
	page = opts.page
else:
	page = 100
if opts.file:
	file = opts.file
	if path.exists(file):
		chdir(file)
	else:
		print('[ERROR] File Not Found')
		exit()
else:
	file = None
if opts.thr:
	thr = opts.thr
else:
	thr = 10
chdir('m')
#d = imgflip()
#d.get_memes(1)
l = lefunny()
tl = l.dump_list()
for n,w in tl.items():
	print(f'[{n}] {w[0]}')
v = input('>>> ')
link = tl[int(v)][1]
l.get_memes(1,link)