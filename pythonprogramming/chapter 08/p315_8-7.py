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
def isperfect(num):
	mList = getfactors(num)
	sum = 0
	for i in mList:
		sum += i
	if sum == num:
		return mList
	return False

if __name__ == '__main__':
	for i in range(1000):
		result = isperfect(i)
		if result:
			print i,isperfect(i)
	
