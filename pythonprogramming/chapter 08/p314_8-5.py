# -*- coding: utf-8 -*-
#
def getfactors(num):
	m = num / 2
	mList = [1,]
	while m > 1:
		if num % m == 0:
			mList.append(m)
		m -= 1
	return mList
	
if __name__ == '__main__':
	while True:
		num = raw_input('Enter your number: > ')
		if num == 'q':
			break
		print getfactors(int(num))
