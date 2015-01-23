# -*- coding: utf-8 -*-
#
#从前向后找
def comp(num):
	n = 0
	for i in range(1,len(num)):
		if num[i] in ('+','-'):
			n += 1
		if n == 2:
			break
	return complex(float(num[:i]),float(num[i:-1]))
#从后向前找，更方便
def compB(num):
	i = 0
	length = len(num)
	for i in range(1,len(num))[::-1]:
		if num[i] in ('+','-'):
			break
	return complex(float(num[:i]),float(num[i:-1]))
if __name__ == '__main__':
	while True:
		num = raw_input('Enter a num, I will turn it to a complex: > ')
		try:
			print comp(num)
			print compB(num)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			break
