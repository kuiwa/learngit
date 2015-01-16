# -*- coding: utf-8 -*-
#
'readTextFile.py -- read and display text file'
import os
# get filename
fname = raw_input('Enter filename: ')
print

# attempt to open file for reading
if os.path.exists(fname):
	with open(fname, 'r') as fobj:
		for eachLine in fobj:
			print eachLine.strip()
else:
	print "*** file open error:"
"""try:
	fobj = open(fname, 'r')
except IOError, e:
	print "*** file open error:", e
else:
	# display contents to the screen
	for eachLine in fobj:
		print eachLine,
	fobj.close()"""
