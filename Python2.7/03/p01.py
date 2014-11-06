#!/usr/bin/env python
# -*- coding: utf-8 -*-

# %字符串格式化
print "Int %d, Float %d, String '%s'" % ( 5, 2.4, 'hello')

box = { 'fruits': ['apple','orange'], 'money': 1993, 'name': 'obama'}
print box['fruits']

b = [ 0, 1, 2, 3]
[ c=var*var for var in b if var < 3 ]
