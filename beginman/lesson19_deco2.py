# -*- coding: utf-8 -*-

def deco1(func):
	print 'ok'
	return func
	
@deco1
def foo():
	print 'foo'

foo()