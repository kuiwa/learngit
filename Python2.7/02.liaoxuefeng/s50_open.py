#!/usr/bin/env python
# -*- coding: utf-8 -*-

#��д�ļ�
f = open('readme.txt', 'r')
#f = open('test.jpg', 'rb')
#��ȡ�������ļ�����ͼƬ����Ƶ��
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