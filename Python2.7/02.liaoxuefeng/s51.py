#!/usr/bin/env python
# -*- coding: utf-8 -*-

#操作文件和目录
import os
print os.name
#系统名称
print os.environ
#环境变量
print os.getenv('PATH')
#获得PATH变量
print os.path.abspath('.')
#查看当前目录的绝对路径
new_dir = os.path.join(os.path.abspath('.'), 'testdir')
#在当前路径下增加一个目录
print new_dir
os.mkdir('new_dir')
#创建目录
os.rmdir('new_dir')
#删除目录
split_dir = os.path.split(new_dir)
print split_dir
#打印出的结果会在每个\前面多增加一个转义字符\
print os.path.splitext('path/to/file.txt')

import shutil
shutil.copyfile('readme.txt', 'test.txt')
os.rename('test.txt','test.py')
os.remove('test.py')

x = 1
for x in os.listdir('.'):
	if os.path.isfile(x) and os.path.splitext(x)[1]=='.py':
		print x