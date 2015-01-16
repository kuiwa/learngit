# -*- coding: utf-8 -*-
#
def sort_abc(a, b, c):
	min = a
	max = a
	med = a
	for i in [a, b, c]:
		if min > i:
			min = i
		elif max < i:
			max = i
	for i in [a, b, c]:
		if i != min and i != max:
			med = i
	return min, med, max


tag = True
while tag:
	try:
		a = raw_input('Enter Number a: ')
		b = raw_input('Enter Number b: ')
		c = raw_input('Enter Number c: ')
		a = int(a)
		b = int(b)
		c = int(c)
		tag = False
	except ValueError as valueerr:
		print 'Error: ' + str(valueerr)
print sort_abc(a, b, c)