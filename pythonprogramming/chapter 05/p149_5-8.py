# -*- coding: utf-8 -*-
#
import math
def areaOrVolume(type, r):
	if type == '1':	# square
		result = r ** 2
	elif type == '2':	# cube
		result = r ** 3
	elif type == '3':	# circle
		result = math.pi * r ** 2
	elif type == '4':	# sphere
		result = (3.0/4) * math.pi * r ** 3
	else:
		result = 'Wrong Number!'
	return result
if __name__ == '__main__':
	while True:
		print '(1) Square'
		print '(2) Cube'
		print '(3) Circle'
		print '(4) Sphere'
		type = raw_input('Enter number: > ')
		r = raw_input('Enter number: > ')
		try:
			floatR = float(r)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			result = areaOrVolume(type, floatR)
			print result
			if result != 'Wrong Number!':
				break