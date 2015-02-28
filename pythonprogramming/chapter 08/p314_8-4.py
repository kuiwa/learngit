# -*- coding: utf-8 -*-
#
def isprime(num):
	m = num / 2 
	while m > 1:
		if num % m == 0:
			return False
		m -= 1
	else:
		return True
if __name__ == '__main__':
	while True:
		num = raw_input('Enter a number:> ')
		if num == 'q':
			break
		print isprime(int(num))
