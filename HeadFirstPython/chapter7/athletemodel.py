# -*- coding: utf-8 -*-
# file: chapter7/athletemodel.py
#
import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return(AthleteList(templ.pop(0), templ.pop(0), templ))
	except IOError as ioerror:
		print("The Error is " + str(ioerror))
		return(None)
def put_to_store(file_list):
	all_athletes = {}
	for file in file_list:
		ath = get_coach_data(file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print ('File error(put_to_store): ' + str(ioerr))
	return(all_athletes)
def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle','rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print ('File error(get_from_store): ' + str(ioerr))
	return(all_athletes)
