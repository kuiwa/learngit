# -*- coding: utf-8 -*-
#
def yearRun(y):
	if (y % 4 == 0 and y% 100 != 0) or (y / 4 % 100 == 0):
		value = 1
	else:
		value = 0
	return value
while True:
	year = raw_input('Enter a year number: > ')
	try:
		intYear = int(year)
	except ValueError as e:
		print 'Error: ' + str(e)
	else:
		if 0 < intYear:
			break
		else:
			print 'Number of year must be a positive inter!'
if yearRun(intYear):
	print '%s is Run Year!' % intYear
else:
	print '%s is not Run Year!' % intYear
