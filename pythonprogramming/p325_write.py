# -*- coding: utf-8 -*-
#
import os
filename = raw_input('Please enter a new file name:> ')
f = open(filename, 'w')
while True:
	eachLine = raw_input("Enter a line ('.' to quit): ")
	if eachLine != '.':
		f.write('%s%s' % (eachLine, os.linesep))
	else:
		break
f.close()
