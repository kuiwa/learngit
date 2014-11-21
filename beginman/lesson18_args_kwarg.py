# -*- coding: utf-8 -*-

def complex_fuction(a, b=None, *args,**kwarg):
	pass

def add(a, b, c):
	return a + b + c
	
print add(a=10,b=10,c=10)
args = (2,3)
print add(1, *args)
kwargs = {'b': 100, 'c': 200}
print add(100, **kwargs)
print add(a=100, **kwargs)
print add(1,2,c=3)