# -*- coding: utf-8 -*-

def convert(argfunc, seq):
	return [argfunc(obj) for obj in seq]
	
lis = [123, 15.23, -6.2e5, 999999999L]
print convert(int, lis)
print convert(float, lis)
print convert(long, lis)