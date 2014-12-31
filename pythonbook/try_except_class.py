# -*- coding: utf-8 -*-
# file: try_except_class.py
#
class MyError(Exception):
	def __init__(self,data):
		self.data = data
	def __str__(self):
		return self.data
try:
	raise MyError('Raise MyError class')
except MyError as data:
	print data
else:
	print 'No Error'