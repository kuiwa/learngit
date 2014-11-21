# -*- coding: utf-8 -*-

# http://www.cnblogs.com/huxi/archive/2011/07/14/2106863.html

def get_0_1_2():
	yield 0
	yield 1
	yield 2
	
generator = get_0_1_2()
print generator.next()
print generator.next()
print generator.next()