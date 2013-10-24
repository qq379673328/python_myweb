#! /usr/bin/env python
#coding=utf-8

import os

#读取某个文件，以只读的方式-r
filepath = "C:\\Users\\sinosoft\\Desktop\\test.txt"
fileHandleR = file(filepath,"r")
for oneline in fileHandleR.readlines():
	print oneline
#读取某个文件，以添加的方式-a
fileHandleA = file(filepath,"a")
fileHandleA.write("\nhaha")
#读取某个文件，以写的方式,会清空文件内容-w
#fileHandleW = file(filepath,"w")

#执行cmd命令
#print os.popen('gvim '+filepath).readlines()
print os.popen('ls').readlines()
