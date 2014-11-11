#!/usr/bin/env python
# -*- coding: utf-8 -*-

#¥ÌŒÛ¥¶¿Ì
#err.py
import logging

def foo(s):
	return 10 / int(s)
	
def bar(s):
	return foo(s) * 2
	
def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)
		
main()
print 'END'

class FooError(StandardError):
	pass
	
def foo_a(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

foo_a(0)