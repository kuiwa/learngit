# -*- coding: utf-8 -*-

def multiply2(**kwargs):
	for key, value in kwargs.items():
		print '%s=>%s' % (key,value)
		
lis = {'name':'beginman'}
multiply2()
multiply2(**lis)
multiply2(name='beginman',age='22',tel=110)