# -*- coding: utf-8 -*-

def multiply(*args):
	total = 1
	for arg in args:
		total += arg
	return total
	
print multiply()
print multiply(1,2)
print multiply(4,5,6,7)