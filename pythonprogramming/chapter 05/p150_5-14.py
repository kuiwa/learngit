# -*- coding: utf-8 -*-
#
"银行复利"
def yearReturns(rate):
	returns = 1
	for i in range(365):
		returns = returns * (1 + rate/365)
	return returns
	
if __name__ == '__main__':
	while True:
		rate = raw_input('Enter rate: >')
		try:
			rateF = float(rate)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			print yearReturns(rateF)
