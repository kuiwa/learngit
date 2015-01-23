# -*- coding: utf-8 -*-
#
" find the mistake in this program"
'''already correct, 将列表中可以被列表长度整除的项删除'''
#
num_str = raw_input('Enter a number: ')
#
num_num = int(num_str)
#
fac_list = range(1, num_num+1)
print 'BEFORE:', fac_list
#
i = 0
#
while i < len(fac_list):
#
	if num_num % fac_list[i] == 0:
		del fac_list[i]
	i = i + 1
print 'AFTER:', fac_list