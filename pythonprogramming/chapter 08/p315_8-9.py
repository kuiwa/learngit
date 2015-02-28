# -*- coding: utf-8 -*-
#
def fibonacci(n):
	a,b = 0,1
	for i in range(n):
		yield a
		a,b = b,a+b
n = raw_input('Enter a number for fabonacci:>')		
print list(fibonacci(int(n)))