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
with open('james.txt') as jaf:
	data = jaf.readline()
	james = data.strip().split(',')
with open('julie.txt') as juf:
	data = juf.readline()
	julie = data.strip().split(',')
with open('mikey.txt') as mif:
	data = mif.readline()
	mikey = data.strip().split(',')
with open('sarah.txt') as saf:
	data = saf.readline()
	sarah = data.strip().split(',')
#clean_james = []
#clean_julie = []
#clean_mikey = []
#clean_sarah = []
#for each_t in james:
#	clean_james.append(sanitize(each_t))
#for each_t in julie:
#	clean_julie.append(sanitize(each_t))
#for each_t in mikey:
#	clean_mikey.append(sanitize(each_t))
#for each_t in sarah:
#	clean_sarah.append(sanitize(each_t))
clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]
#print(james)
#print(sorted(james))
print(sorted([sanitize(each_t) for each_t in james]))
#print(julie)
#print(sorted(julie))
print(sorted([sanitize(each_t) for each_t in julie]))
#print(mikey)
#print(sorted(mikey))
print(sorted([sanitize(each_t) for each_t in mikey]))
#print(sarah)
#print(sorted(sarah))
print(sorted([sanitize(each_t) for each_t in sarah]))

