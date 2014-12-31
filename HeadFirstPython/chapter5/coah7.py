# -*- coding: utf-8 -*-
# file: coah.py
#
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)
def sort_data(txt):
	try:
		with open(txt) as file:
			data = file.readline()
			dirty = data.strip().split(',')
			#clean = sorted([sanitize(t) for t in dirty])
			#unique_data = []
			#for t in clean:
			#	if not t in unique_data:
			#		unique_data.append(t)
			unique_data = sorted(set([sanitize(t) for t in dirty]))
		return unique_data
	except IOError as ioerror:
		print('File error: ' + str(ioerror))
		return(None)
james = sort_data('james.txt')
julie = sort_data('julie.txt')
mikey = sort_data('mikey.txt')
sarah = sort_data('sarah.txt')
print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])