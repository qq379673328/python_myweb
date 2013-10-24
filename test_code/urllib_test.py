#! /usr/bin/env python
#coding=utf-8

import urllib2
import urllib
from HTMLParser import HTMLParser

#需要解析的网址
url = 'http://www.ithome.com'
#储存文件的根路径
basepath = 'C:\\Users\\sinosoft\\Desktop\\testdown'

html = urllib2.urlopen(url).read()

#自定义html解析方式
class MyHtmlParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		#过滤图片
		if tag == 'img':
			for attr in attrs:
				if attr[0] == 'src':
					#页面上所有img-src图片的地址
					imgsrc = attr[1]
	def handle_endtag(self, tag):
		pass
	def handle_data(self, data):
		pass

myParser = MyHtmlParser()
myParser.feed(html)
