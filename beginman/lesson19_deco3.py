# -*- coding: utf-8 -*-

def deco1(func):
	print "deco1"
	return func
	
def deco2(func):
	print "deco2"
	return func
	
@deco1
@deco2
def foo():
	print "foo"
	
#foo()