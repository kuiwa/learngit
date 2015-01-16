# -*- coding: utf-8 -*-
#
def changeCoin(dollar):
	numCoin = []
	for coin in (25,10,5,1):
		i,j = divmod(dollar, coin)
		numCoin.append(i)
		dollar = j
	return numCoin
if __name__ == '__main__':
	while True:
		dollar = raw_input('Enter your dollar number: 1-99 > ')
		try: 
			intDollar = int(dollar)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			if 0 < intDollar < 100:
				break
			else:
				print 'Number range: 1-99'
	l = changeCoin(int(dollar))
	print "$25 is %s, $10 is %s, $ 5 is %s, $1 is %s." % (l[0],l[1],l[2],l[3])

