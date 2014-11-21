# -*- coding: utf-8 -*-

seq = [11,10,9,9,5,35,8,20,31,72,54,53]
f1 = filter(lambda x: x%2, seq)
print f1
f2 =  [x for x in seq if x%2]
print f2

f3 = [(x+1,y+1) for x in range(3) for y in range(5)]
print f3
f4 = [(x,y) for x in range(3) for y in range(3)]
print f4

for x in range(3):
	for x in range(3):
		print x,y