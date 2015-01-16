# -*- coding: utf-8 -*-
#
def changeCoin(dollar):
	numCoin = []
	for coin in (25,10,5,1):
		i,j = divmod(dollar, coin)
		numCoin.append(i)
		dollar = j
	return numCoin
def isLessThan100(num):
	try:
		intNum = int(num)
	except ValueError as e:
		print 'Error: ' + str(e)
		return False
	else:
		if 0 < int(num) < 100:
			return True
		else:
			return False
if __name__ == '__main__':
	while True:
		dollar = raw_input('Enter your dollar number: 1-99 > ')
		if isLessThan100(dollar):
			l = changeCoin(int(dollar))
			print "$25 is %s, $10 is %s, $ 5 is %s, $1 is %s." % (l[0],l[1],l[2],l[3])
			break
		else:
			print "Wrong number"
