# -*- coding: utf-8 -*-

def add(x,y): return x+y
add2 = lambda x,y: x+y
print add2(1,2)

def sum(x,y): return x+y
sum2 = lambda x,y=10: x+y
print sum2(1)
print sum2(1,100)