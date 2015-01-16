# -*- coding: utf-8 -*-
#
from __future__ import division
def F2C(temp):
	C = (temp - 32) * (5 / 9)
	return C
def C2F(temp):
	F = temp / (5 / 9) + 32
	return F
if __name__ == '__main__':
	while True:
		print '(1) transfer F temperature to C'
		print '(2) transfer C temperature to F'
		fun = raw_input('Enter 1 or 2: >')
		if fun != '1' and fun != '2':
			print 'Wrong Choice! Enter again.'
			continue
		temp = raw_input('Enter temperature: > ')
		try:
			tempFloat = float(temp)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			if fun == '1':
				Temp = F2C(tempFloat)
			elif fun == '2':
				Temp = C2F(tempFloat)
			print '%sF equals %sC' % (tempFloat, Temp)
			break