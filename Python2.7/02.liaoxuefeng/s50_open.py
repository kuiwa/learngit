#!/usr/bin/env python
# -*- coding: utf-8 -*-

#读写文件
f = open('readme.txt', 'r')
#f = open('test.jpg', 'rb')
#读取二进制文件，如图片、视频等
print f.read()
f.close()

try:
	f = open('readme.txt', 'r')
	print f.read()
finally:
	if f:
		f.close()
		print 'Closed the file!'
		
with open('readme.txt', 'r') as f:
	print f.read()
	
with open('readme.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip())