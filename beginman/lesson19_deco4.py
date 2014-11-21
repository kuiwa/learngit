# -*- coding: utf-8 -*-

from time import ctime, sleep

def deco(func):
	def decoIn():
		print '[%s]:%s called' % (ctime(), func.__name__)
		return func
	return decoIn
	
@deco
def foo():
	print "foo"
	
#foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()