# -*- coding: utf-8 -*-
#
def displayNumType(num):
	print num, ' is ',
	if isinstance(num,(int, long, float, complex)):
		print 'a number of type: ', type(num).__name__
	else:
		print 'not a number at all!!'

for num in [-69, 99999999999L, 98.6, -5.2+1.9j, 'xxx']:
		displayNumType(num)
