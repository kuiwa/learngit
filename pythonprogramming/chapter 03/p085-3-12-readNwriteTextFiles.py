# -*- coding: utf-8 -*-
#
'readNwriteTextFiles.py -- create text file'

import os

def writeText():
	ls = os.linesep
	# get filename
	while True:
		fname = raw_input('filename> ')
		if os.path.exists(fname):
			print "ERROR: '%s' already exists" % fname
		else:
			break
			
	# get file content (text) lines
	all = []
	print "\nEnter lines ('.' by itself to quit). \n"

	# loop until user terminates input
	while True:
		entry = raw_input('> ')
		if entry == '.':
			break
		else:
			all.append(entry)
			
	# write lines to file with proper line-ending
	fobj = open(fname, 'w')
	fobj.writelines(['%s%s' % (x, ls) for x in all])
	fobj.close()
	print 'DONE!'
	
def readText():
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
	
if __name__ == '__main__':
	print "Choose 1 or 2 for write or read a text file: "
	print "1. WriteTextFile"
	print "2. ReadTextFile"
	choose = raw_input('> ')
	if choose == '1':
		writeText()
	elif choose == '2':
		readText()
	else:
		print "Wrong Number!!"
