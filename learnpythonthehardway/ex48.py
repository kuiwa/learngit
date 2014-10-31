# -*- coding:utf-8 -*-

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
		
s = 'string'
print convert_number(s)

