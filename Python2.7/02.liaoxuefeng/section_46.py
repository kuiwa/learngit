#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ต๗สิ
#assert
#python -O section_46.py  close the assert
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n
	
def main():
	foo('0')
	
#main()