# -*- coding: utf-8 -*-
#
import random
#显示一个水平或垂直排序的矩阵列表
def show(aList, num, style=True):
	aList.sort()
	length = len(aList)
	row = int(num)
	interval = length // row
	matrix = []
	i = 0
	j = 0
	while j < row - 1:
		matrix.append(aList[i:i+interval])
		i += interval
		j += 1
	matrix.append(aList[i:])
	if not style:
		return changeList(matrix)
	print '水平显示'
	return matrix
#矩阵的反转	
def changeList(aList):
	row = len(aList)
	col = len(aList[0])
	num = []
	subNum = []
	for i in range(col):
		for j in range(row):
			subNum.append(aList[j][i])
		num.append(subNum)
		subNum = []
	return num

lst = []
length = 47
for i in range(length):
	lst.append(random.randrange(100)) 
print lst
while True:
	print 'There is a list with %d elements.' % length
	style = raw_input('Do you want to show the list horizontally(False for no): > ')
	if style != False:
		style = True
	num = raw_input('Enter the num of col(row): > ')
# use random to generate a new list
	matrix = show(lst, num, style)
	for i in matrix:
		print i
	break