# -*- coding: utf-8 -*-

import time

def timeit(func):
		start = time.clock()
		func
		end = time.clock()
		print 'used: ', end - start
	
timeit(map(lambda x:x*10,[i for i in range(10)]))

timeit(x*10 for x in range(10))