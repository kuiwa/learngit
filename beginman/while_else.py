# -*- coding: utf-8 -*-

def showMaxFactor(num):
	count = num / 2
	while count > 1:
		if num % count == 0:
			print u'%d 的最大公约数是: %d' % (num, count)
			break
		count -= 1
	else:
		print num, u'是素数'
	
for eachNum in range(10,21):
	showMaxFactor(eachNum)