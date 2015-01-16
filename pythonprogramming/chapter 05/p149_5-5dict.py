# -*- coding: utf-8 -*-
#
"Use dict to implement 5-5"
def change(coin):
	coins = {25:0, 10:0, 5:0, 1:0}
	for i in coins:
		v, coin = divmod(coin, i)
		coins[i] = v
	return coins

if __name__ == '__main__':
	while True:
		coin = raw_input('Enter Coins number: >')
		try:
			coinInt = int(coin)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			if coinInt < 100:
				coins = change(coinInt)
				for i in coins:
					print '%s is %s' % (i, coins[i])
				break
			else:
				print 'Coins must be less than 100!'