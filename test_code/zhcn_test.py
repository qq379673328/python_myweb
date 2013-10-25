#! /usr/bin/env python
#coding=utf-8

'''
中文相关
'''

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

testpath = 'E:\\python_workspace\\python_myweb\\python_myweb\\test_code\\testpath'
filename = '你好'
print filename.encode('gbk')