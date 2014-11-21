# -*- coding: utf-8 -*-

try:
	f = open('d.txt', 'r')
	try:
		f.seek(100,2)
		fshow = f.read(1000)
	finally:
		f.colse()
	except IOError:
	pass
	