#!/usr/bin/env python
# -*- coding: utf-8 -*-

#定制类
#__repr__
#__call__
#__getattr__
class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__
	def __call__(self):	#增加后，可以直接调用对象自身
		print('My name is %s.' % self.name)
	def __getattr__(self, attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda: 25	#返回函数
		raise AttributeError('\'Student\' object has no attribut \'%s\'' % attr)	#调用没有的属性时，打印出错误
print Student('Michael')
s = Student('Michael')
print s
print s.score
print s()
print s.age()	#lambda的调用方式
#print s.home	#AttributeError错误
print callable(Student())
print callable(max)
print callable(None)

#__iter__
#__getitem__
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
		
	def __iter__(self):
		return self
		
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration();
		return self.a
		
	def __getitem__(self, n):	#Fib开始支持[]
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):	#增加了对切片的处理能力
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

i = 0		
for n in Fib():
	print n
	i += 1
print i
f = Fib()
print f[3]
print f[100]
print f[0:5]