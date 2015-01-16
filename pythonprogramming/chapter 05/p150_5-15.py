# -*- coding: utf-8 -*-
#
" calculate greatest common divisor and lowest common multiple"
def max(a, b):
	if a < b:
		return (b, a)
	else:
		return (a, b)
def gcd(a, b):
	big, small = max(a, b)
	if big % small == 0:
		return small
	else:
		for i in range(small//2+1, 0, -1):
			if a % i == 0 and b % i == 0:
				return i
def lcm(a, b):
	big, small = max(a, b)
	div = 1
	if big % small == 0:
		return big
	else:
		for i in range(small//2+1, 0, -1):
			if big % i == 0 and small % i == 0:
				div = div * i
				big = big / i
				small = small / i
		return (div * big * small)
if __name__ == '__main__':
	while True:
		a = raw_input('Enter Number a: >')
		b = raw_input('Enter Number b: >')
		try:
			aInt = int(a)
			bInt = int(b)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			print gcd(aInt, bInt)
			print lcm(aInt, bInt)
			break