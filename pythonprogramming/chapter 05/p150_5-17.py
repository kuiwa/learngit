# -*- coding: utf-8 -*-
#
"Use random module"
import random
def createList(N, n):
	numList = []
	for i in range(N):
		numList.append(random.randint(-1,n))
	return numList
def sortList(N):
	numList = createList(100, 2**31)
	randList = []
	for i in range(N):
		r = random.randint(0,N)
		randList.append(numList[r])
	# bubble sort
	'''for i in range(len(randList)):
		for j in range(len(randList)-1):
			if randList[j+1] < randList[j]:
				randList[j+1], randList[j] = randList[j], randList[j+1]'''
	randList.sort()
	return randList
	
if __name__ == '__main__':
	while True:
		n = raw_input('Enter the randList number: >')
		try:
			nInt = int(n)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			randList = sortList(nInt)
			for i in randList:
				print i,
			print