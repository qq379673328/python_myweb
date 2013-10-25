#! /usr/bin/env python
#coding=utf-8

import urllib2
import urllib
from HTMLParser import HTMLParser

#配置参数
#请求页面
url = 'http://www.ithome.com'
#存放目录
folder = 'ithome'
#下载数目
limit = 5
#储存文件的根路径
basepath = 'E:\\python_workspace\\python_myweb\\python_myweb\\test_code\\down'

#文档内容
html = urllib2.urlopen(url).read()

#自定义html解析方式
class MyHtmlParser(HTMLParser):
	count = 0
	def handle_starttag(self, tag, attrs):
		#过滤图片
		if tag == 'img':
			for attr in attrs:
				if attr[0] == 'src' and self.count < limit:
					self.count += 1
					#页面上所有img-src图片的地址
					imgsrc = attr[1]
					#获取图片名-格式类似-http://ip/10/56268.jpg
					imgsplit = imgsrc.split('/')
					imgsplitlen = len(imgsplit)
					imgname = imgsplit[imgsplitlen-1]
					urllib.urlretrieve(imgsrc, basepath+'\\'+folder+'\\'+imgname)

	def handle_endtag(self, tag):
		pass
	def handle_data(self, data):
		pass

myParser = MyHtmlParser()
myParser.feed(html)
