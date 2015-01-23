# -*- coding: utf-8 -*-
#
" WWWXXXYYYZZZ to WWW.XXX.YYY.ZZZ "
def num2ip(num):
	try:
		num12 = '%012d' % int(num)
	except ValueError as e:
		print 'Error: ' + str(e)
		return False
	else:
		print '%s.%s.%s.%s' % (num12[0:3],num12[3:6],num12[6:9],num12[9:])
		return True
def ip2num(ip):	
	aList = []
	try:
		for i in ip.split('.'):
			aList.append(int(i))
		num = '%d%03d%03d%03d' % (aList[0],aList[1],aList[2],aList[3])
	except (ValueError, IndexError) as e:
		print 'Error: ' + str(e)
		return False
	else:
		print num
		return True
print 'This program turns a number to IP address'
while True:
	data = raw_input('Enter a number or a IP address: > ')
	if '.' not in data:
		exit = num2ip(data)
	else:
		exit = ip2num(data)
	if exit:
		break
