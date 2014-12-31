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
	with open(txt) as file:
		data = file.readline()
		dirty = data.strip().split(',')
		clean = sorted([sanitize(t) for t in dirty])
		unique_data = []
		for t in clean:
			if not t in unique_data:
				unique_data.append(t)
	return unique_data
james = sort_data('james.txt')
print(james[0:3])