# -*- coding: utf-8 -*-

def foo(arg, obj1='good', obj2='10'):
	return arg, obj1, obj2
	
print foo(arg='BeginMan')
print foo('BeginMan')
print foo('BeginMan', 'Python')
print foo(arg='BeginMan', obj2=100)
print foo(obj2=100, arg='BeginMan',obj1='OK')