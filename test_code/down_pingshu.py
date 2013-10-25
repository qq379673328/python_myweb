#! /usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import os
from HTMLParser import HTMLParser

''' 次文件用于从 www.5tps.com 下载评书 '''

#配置参数
#请求页面
url = 'http://www.5tps.com'
#存放目录
folder = 'pingshu_luanshixiaoxiong'
#下载数目
limit = 1 
#储存文件的根路径
basepath = 'E:\\python_workspace\\python_myweb\\python_myweb\\test_code\\down'
#文档内容-某篇评书
bookpage = '/html/3114.html'


headers = { #伪装为浏览器抓取
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}

#自定义请求页面函数
def requestOnePage(url):
	return urllib2.urlopen(urllib2.Request(url, headers=headers)).read()

#请求页面，并获取内容
class RequestPage():
	def __init__(self):
		pass
	def getHtml(self):
		urllib2.urlopen(url+bookpage).read()

#解析下载页面
class MyHtmlParser(HTMLParser):
	count = 0
	downpagelist = []
	def handle_starttag(self, tag, attrs):
		#过滤下载链接
		if tag == 'a':
			for attr in attrs:
				if attr[0] == 'href' and len(attr[1].split('/')) > 2 and attr[1].split('/')[1] == 'down':
					#记录下载页面
					self.downpagelist.append(url+attr[1])

	def handle_endtag(self, tag):
		pass
	def handle_data(self, data):
		pass

#下载进度使用
def Schedule(a,b,c):
	per = 100.0*a *b /c
	if per > 100:
		per = 100
	print'%.2f%%' % per

#解析下载链接并下载
class ParserDown(HTMLParser):
	isdown = False
	def handle_starttag(self, tag, attrs):
		#过滤下载地址
		if tag == 'a':
			for attr in attrs:
				if attr[0] == 'href' and ('.mp3' in attr[1]):
					#下载
					src = attr[1]
					filename = src.split('/').pop().split('?')[0]
					filepath = basepath+'\\'+folder+'\\'+filename
					if os.path.isfile(filepath):
						print 'File['+filepath+'] already download.'
						return
					print 'Down file:'+filename
					urllib.urlretrieve(src, filepath)
					print 'Success...'
					self.isdown = True

	def handle_endtag(self, tag):
		pass
	def handle_data(self, data):
		pass

#文档内容-某篇评书
html = requestOnePage(url+bookpage)
myParser = MyHtmlParser()
myParser.feed(html)
#下载数目记录
count = 0
#新建目录
if not os.path.exists(basepath+'\\'+folder):
	os.mkdir(basepath+'\\'+folder)

#总数目
print 'Total count:' + str(len(myParser.downpagelist))

#下载文件
for onedown in myParser.downpagelist:
	if limit == count:#达到最大数据-停止下载
		break
	print 'Open page:'+onedown
	parserDown = ParserDown()
	parserDown.feed(requestOnePage(onedown))
	if parserDown.isdown:
		count += 1
