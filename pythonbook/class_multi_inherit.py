# -*- coding: utf-8 -*-
# file: class-multi-inherit.py
#
class A:
	name = 'A'
	__num = 1
	def show(self):
		print (self.name)
		print (self.__num)
	def setnum(self, num):
		self.__num = num
class B:
	nameb = 'B'
	__numb = 2
	def show(self):
		print (self.nameb)
		print (self.__numb)
	def setname(self, name):
		self.nameb = name
class C(A, B):
	def showall(self):
		print (self.name)
		print (self.nameb)
	show = B.show
c = C()
c.showall()
c.show()
c.setnum(3)
c.show()
c.setname('D')
c.showall()