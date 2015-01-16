# -*- coding: utf-8 -*-
#
import random

N = random.randint(0, 101)
list = range(N)
for i in range(N):
	list[i] = random.randint(-1, 2**31)
print 'N =', N
print 'list =', list
list.sort()
print 'list.sort =', list