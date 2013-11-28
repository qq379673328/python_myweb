#! /usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import os
import sys
import threading
import time
import re
from HTMLParser import HTMLParser

''' 通过页面链接批量下载资源 '''

#设置编码
reload(sys)
sys.setdefaultencoding('utf-8')

'''配置参数'''

'''资源相关'''
remoteparam = {
		'domain':'http://www.5tps.com',#必须
		'page':'http://www.5tps.com/html/11655.html'#必须
		}

'''本地参数'''
localparam = {
		'limit':10,#资源数限制-可选
		'localpath':'E:\\download',#根目录-必须
		'title':'皮皮鲁外传'#目录名-必须
		}

##########################################################

enabledomain = {#可解析域名组
		'http://www.5tps.com':{

			}
		}

headers = { #伪装为浏览器抓取
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}

#自定义请求页面函数
def requestOnePage(url):
	return urllib2.urlopen(urllib2.Request(url, headers=headers)).read()

#解析页面-属性值与正则匹配
class SelfHtmlParse(HTMLParser):
	def __init__(self, goal, regexp):
		self.goal = goal#down or parse
		self.count = 0
		self.downpagelist = []
		self.regexp = regexp
	def handle_starttag(self, tag, attrs):
		if self.goal == 'down':
			src = attrs[1]
			filepath = ''
			filename = ''
			if re.complie(regexp).match(src):
				print 'src:',src
				print 'filepath:',filepath
				print 'filename:',filename
				#new DownFile(src, filepath, filename).run()
			pass #下载
		elif self.goal == 'parse':
			pass #继续解析
		else:
			pass #TODO:
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

''' 下载一个文件-开辟新线程 '''
class DownFile(threading.Thread):
	def __init__(self, src, filepath, filename):
		threading.Thread.__init__(self)
		self.src = src
		self.filepath = filepath
		self.filename = filename
		self.thread_stop = False
	def run(self):
		while not self.thread_stop:
			if os.path.isfile(self.filepath):
				print 'File['+self.filename+'] already download.'
				return
			print 'Thread (%s), Time:%s begin...\n' %(self.filename, time.ctime())
			urllib.urlretrieve(self.src, self.filepath)
			print self.filename + ' 下载完毕...'.encode('gbk')
	def stop(self):
		self.thread_stop = True

oneparse = SelfHtmlParse('down', '*.com')
onepage = requestOnePage('http://www.aqee.net/')
oneparse.feed(onepage.encode('gbk'))
