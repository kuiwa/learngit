# -*- coding: utf-8 -*-

bar = 10
def foo():
	global bar
	return bar
	
bar = 10000
print foo()