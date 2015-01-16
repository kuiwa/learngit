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
	
def readText(fname=None):
	# get filename
	if fname == None:
		fname = raw_input('Enter filename: ')
	print

	# attempt to open file for reading
	if os.path.exists(fname):
		with open(fname, 'r') as fobj:
			for eachLine in fobj:
				print eachLine.strip() + '\n'
	else:
		print "*** file open error:"

# still has some error in editText() function
def editText():
	ls = os.linesep
	# get filename
	fname = raw_input('Enter filename: ')
	readText(fname)
	line = raw_input('Which line do you want to edit? > ')
	li = []
	try:
		with open(fname, 'r') as f:
			for i,eachLine in enumerate(f):
				if i == int(line) - 1:
					eachLine = raw_input('Enter your words: ')
				li.append(eachLine)
				#li.append('\n')
	except IOError as ioerr:
		print "Error: " + str(ioerr)
	with open(fname, 'w') as f:
		f.writelines([ '%s%s' % (x, ls) for x in li])
	print 'DONE!'
			
if __name__ == '__main__':
	print "Choose 1 or 2 for write or read a text file: "
	print "1. WriteTextFile"
	print "2. ReadTextFile"
	print "3. EditTextFile"
	choose = raw_input('> ')
	if choose == '1':
		writeText()
	elif choose == '2':
		readText()
	elif choose == '3':
		editText()
	else:
		print "Wrong Number!!"
