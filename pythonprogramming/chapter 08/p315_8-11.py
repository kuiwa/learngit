# -*- coding: utf-8 -*-
#
def nameFormat(num):
	wrongNum = 0
	nameList = []
	for n in range(1,num+1):
		name = raw_input('Please enter name %s: ' % n)
		if ',' not in name:
			wrongNum += 1
			print 'Wrong format... should be Last, First.'
			print 'You have done this %s time(s) already. Fixing input...' % wrongNum
			continue
		nameList.append(name)
	print 'The sorted list (by last name) is:'
	for na in nameList:
		print na
		
if __name__ == '__main__':
	num = raw_input('Enter total number of names: ')
	nameFormat(int(num))