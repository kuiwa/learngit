# -*- coding: utf-8 -*-
# file: try_except_raise.py
#
try:
	raise Exception
except Exception:
	print 'Error'
else:
	print 'No Error'
	
try:
	raise Exception, 'Raise an Exception'
except Exception as data:
	print data
else:
	print 'No Error'

def fun(n):
	if n == 0:
		raise ZeroDivisionError('n is zero')
	else:
		print n
try:
	fun(0)
except ZeroDivisionError as data:
	print data
else:
	print 'No Error'
	
class A(Exception):
	def show(self):
		print 'A'
try:
	raise A
except A:
	print ('Error')
else:
	print ('No Error')