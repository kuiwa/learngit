# -*- coding: utf-8 -*-

def isPrime(n):
	"""This function return a number is a prime or not"""
	assert n >= 2
	from math import sqrt
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			return False
	return True
	
isPrime(2)
isPrime(9)