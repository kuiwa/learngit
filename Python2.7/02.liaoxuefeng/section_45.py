#!/usr/bin/env python
# -*- coding: utf-8 -*-


#¥ÌŒÛ¥¶¿Ì
def foo():
	r = some_function()
	if r ==(-1):	
		return(-1)
	return r

def bar():
	r = foo()
	if r==(-1):
		print 'Error'
	else:
		pass

#try...except		
try:
	print 'try...'
	#r = 10 / 0	#test ZeroDivisionError
	#r = 10 / int('a')	#test ValueError
	r = 10 / 2
	print 'result:', r
except ValueError, e:
	print 'ValueError:', e
except ZeroDivisionError, e:
	print 'except:', e
else:
	print 'no error!'
finally:
	print 'finally...'
print 'END'


