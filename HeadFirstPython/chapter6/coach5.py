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
		return Athlete(templ.pop(0), templ.pop(0), templ)
	except IOError as ioerror:
		print('File error: ' + str(ioerror))
		return(None)
class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=None):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
	def add_time(self, a_times):
		self.times.append(a_times)
	def add_times(self, a_times_list):
		self.times.extend(a_times_list)
	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times]))[0:3])
sarah_dict = get_coach_data('sarah2.txt')
print(sarah_dict.name + "'s fastest times are: " + str(sarah_dict.top3()))
sarah_dict.add_time('2.17')
sarah_dict.add_times(['2.16','2.33'])
print(sarah_dict.name + "'s fastest times are: " + str(sarah_dict.top3()))
