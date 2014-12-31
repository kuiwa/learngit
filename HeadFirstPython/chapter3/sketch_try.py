# -*- coding: utf-8 -*-
# file: sketch.py
#
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print (role, end='')
			print (' said: ', end='')
			print (line_spoken, end='')
		except ValueError:
			print ('Here is a error')
	data.close()
except IOError:
	print ('The data file is missing!')