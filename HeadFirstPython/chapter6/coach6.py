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
		return AthleteList(templ.pop(0), templ.pop(0), templ)
	except IOError as ioerror:
		print('File error: ' + str(ioerror))
		return(None)
class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_times=None):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])
sarah_dict = get_coach_data('sarah2.txt')
print(sarah_dict.name + "'s fastest times are: " + str(sarah_dict.top3()))
sarah_dict.append('2.17')
sarah_dict.extend(['2.16','2.33'])
print(sarah_dict.name + "'s fastest times are: " + str(sarah_dict.top3()))
