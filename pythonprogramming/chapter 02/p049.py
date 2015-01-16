# -*- coding: utf-8 -*-
# file: p049.py
# open/
filename = raw_input('Enter file name: ')
data = open(filename, 'r')
for each_line in data:
	print each_line,
data.close()