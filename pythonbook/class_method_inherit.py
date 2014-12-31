# -*- coding: utf-8 -*-
# file: class_method.py
#
class book:
	__author = ''
	__name = ''
	__page = 0
	price = 0
	__press = ''
	def __check(self, item):
		if item == '':
			return 0
		else:
			return 1
	def show(self):
		if self.__check(self.__author):
			print(self.__author)
		else:
			print ('No value')
		if self.__check(self.__name):
			print(self.__name)
		else:
			print 'No name'
	def setname(self, name):
		self.__name = name
	def __init__(self,author,name):
		self.__author = author
		self.__name = name
class student(book):
	__class = ''
	__grade = ''
	__sname = ''
	def showinfo(self):
		self.show()
		
a = book('peter', 'Jack')
a.show()
a.setname('Tom')
a.show()

b = student('Jack','Big Book')
b.showinfo()
b.show()