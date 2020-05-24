#!/usr/bin/env python3
import requests,re,random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 

ua = UserAgent()

class lefunny:
	def __init__(self):
		pass
	def dump_list(self):
		global the_list
		req = requests.get(f'https://lefunny.net',headers={'User-agent':ua.random}).content
		soup = BeautifulSoup(req, "html.parser")
		ancher = soup.find_all('li', {'class': re.compile(r'cat-item cat-item-\d*')})
		x = 0
		d = {}
		for pt in ancher:
			a_tag = pt.find('a')
			the_list = (re.search(r'>.*'.encode('utf-8'),a_tag.encode('utf-8')).group().decode('utf-8').replace('>','').replace(r'</a',''))
			x = x + 1
			d[x] = [f'{the_list}',f'{a_tag["href"]}']
		return d
	def get(self,page,the_link):
		req = requests.get(f'{the_link}page/{page}',headers={'User-agent':ua.random}).content
		soup = BeautifulSoup(req, "html.parser")
		ancher = soup.find_all('div', {'class': "entry-summary"})
		for pt in ancher:
			img = pt.find('img', {'class': 'alignleft post-thumbnail wp-post-image'})
			if img:
				r = requests.get(img['src'],headers={'User-agent':ua.random})
				f = open(img['src'].split('/')[7],'wb')
				f.write(r.content)
				f.close()
class imgflip:
	def __init__(slef):
		pass
	def get_memes(self,page):
		req = requests.get(f'https://imgflip.com/?page={page}',headers={'User-agent':ua.random}).content
		soup = BeautifulSoup(req, "html.parser")
		ancher = soup.find_all('div', {'class': "base-unit clearfix"})
		for pt in ancher:
			img = pt.find('img', {'class': 'base-img'})
			if img:
				link = img['src'].replace(img['src'][0:2],'https://')
				r = requests.get(link,headers={'User-agent':ua.random})
				f = open(img['src'].split('/')[3],'wb')
				f.write(r.content)
				f.close()
