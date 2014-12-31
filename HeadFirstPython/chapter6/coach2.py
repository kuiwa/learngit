# -*- coding: utf-8 -*-
# file: chapter6/coach1.py
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
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return ({'Name': templ.pop(0),
				'DOB': templ.pop(0),
				'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
	except IOError as ioerror:
		print('File error: ' + str(ioerror))
		return(None)
sarah_dict = get_coach_data('sarah2.txt')
print(sarah_dict['Name'] + "'s fastest times are: " + sarah_dict['Times'])