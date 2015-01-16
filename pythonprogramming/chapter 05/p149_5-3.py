# -*- coding: utf-8 -*-
#
def level(num):
	if 90 <= num <= 100:
		l = 'A'
	elif 80 <= num <= 89:
		l = 'B'
	elif 70 <= num <= 79:
		l = 'C'
	elif 60 <= num <= 69:
		l = 'D'
	else:
		l = 'E'
	return l
while True:
	num = raw_input('Enter your score: > ')
	try:
		intNum = int(num)
	except ValueError as e:
		print "Error: " + str(e)
	else:
		if 0 <= intNum <= 100:
			break
		else:
			print "Wrong score (1-100)!"
print level(intNum)