#!/usr/bin/env python3

import requests,re,threading
from bs4 import BeautifulSoup
from queue import Queue
from optparse import OptionParser
from os import chdir,path
from core import *
q = Queue()
__author__ = 'Khaled Nassar'
__link__ = 'https://github.com/knassar702/imge'

print(r'''
{red}
  (_)_ _  ___ ____ 
 / /  ' \/ _ `/ -_)
/_/_/_/_/\_, /\__/ 
        /___/  
{yellow}
[Credits : Khaled Nassar @knassar702]
{end}'''.format(red=red,yellow=yellow,end=end))
lefunny = lefunny()
imgflip = imgflip()
q = Queue()
w = Queue()
# options
optp = OptionParser(add_help_option=False)
optp.add_option("-t","--threads",dest="thr",type='int')
optp.add_option("-f","--file",dest="file")
optp.add_option("-h","--help",dest="help",action='store_true')
optp.add_option("-p","--page",dest="page",type='int')
optp.add_option("-l","--list",dest="the_list",action='store_true')
optp.add_option("-n","--number",dest="_number",type='int')
optp.add_option("-d","--dump",dest="_dump",action='store_true')
optp.add_option("-D","--Dump",dest="_Dump",action='store_true')
opts, args = optp.parse_args()
if opts.help:
	print('''
	-h,--help      | Show help message and exit
	-t,--threads   | Max number of concurrent requests (default: 10)
	-f,--file      | Saving in Custom Path (--file='image_file')
	-p,--page      | number of website pages
	-d,--dump      | Dump Links Without Download
	-l,--list      | Dump all lists
	-D,--Dump      | Dump Links With Download it
	-n,--number    | Number of item (-n=21)
	''')
	exit()
if opts._dump:
	_dump = True
else:
	_dump = None
if opts._Dump:
	_Dump = True
else:
	_Dump = None
if _Dump == True and _dump == True:
	print(f'{yellow}[{red}ERROR{yellow}]{end} You Can"t User --Dump option and --dump in the same time ..!')
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
		print(f'{yellow}[{red}ERROR{yellow}]{end} File Not Found')
		exit()
else:
	file = None
if opts._number:
	lefunny.dump_list()
	_number = opts._number
	if _number > 41:
		print(f'{yellow}[{red}ERROR{yellow}]{end} Number out of Range')
		exit()
	the_link = lefunny.dump_list()[_number][1]
if opts.the_list:
	for n,w in lefunny.dump_list().items():
		print(f'[{n}] {w[0]}')
	exit()
if opts.thr:
	thr = opts.thr
else:
	thr = 10
if opts._number == None:
	print('''
	-h,--help      | Show help message and exit
	-t,--threads   | Max number of concurrent requests (default: 10)
	-f,--file      | Saving in Custom Path (--file='image_file')
	-p,--page      | number of website pages
	-d,--dump      | Dump Links Without Download
	-l,--list      | Dump all lists
	-D,--Dump      | Dump Links With Download it
	-n,--number    | Number of item (-n=21)
	''')
	exit()
def threader_lefunny():
	while True:
		item = q.get()
		lefunny.get(item,the_link,dump=_dump,Dump=_Dump)
		q.task_done()
def threader_imgflip():
	while True:
		item2 = w.get()
		imgflip.get_memes(item2,dump=_dump,Dump=_Dump)
		w.task_done()

if __name__ == '__main__':
	for i in range(thr):
		p1 = threading.Thread(target=threader_lefunny)
		p1.daemon = True 
		p1.start()
		if opts._number == 12: 
			p2 = threading.Thread(target=threader_imgflip)
			p2.daemon = True
			p2.start()
	for i in range(page):
		q.put(i)
		if opts._number == 12: w.put(i)
	try:
		q.join()
		if opts._number == 12: w.join()
	except KeyboardInterrupt:
		print(f'\n{info} Good Bye\n')
