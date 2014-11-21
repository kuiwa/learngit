# -*- coding: utf-8 -*-

def deco(func):
	return func

@deco
def foo():
		print 'foo'
		
foo()