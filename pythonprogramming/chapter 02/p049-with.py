# -*- coding: utf-8 -*-
# file: p049-with.py
# with
filename = raw_input('Enter file name: ')
try:
	with open(filename, 'r') as f:
		for each_line in f:
			print each_line,
except IOError as ioerr:
	print('File error: ' + str(ioerr))
