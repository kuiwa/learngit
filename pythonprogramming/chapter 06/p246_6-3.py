# -*- coding: utf-8 -*-
#
def new_sortA(num):
	aList = []
	lst = num.split()
	return sorted([float(x) for x in lst],reverse=True)
def new_sortB(num):
	aList = []
	aList = num.split()
	aList.sort(reverse=True)
	return aList
if __name__ == '__main__':
	num = raw_input('Please enter numbers with space seperator:> ')
	print new_sortA(num)
	print new_sortB(num)