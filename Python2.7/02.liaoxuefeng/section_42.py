#!/usr/bin/env python
# -*- coding: utf-8 -*-

#������
#__repr__
#__call__
#__getattr__
class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__
	def __call__(self):	#���Ӻ󣬿���ֱ�ӵ��ö�������
		print('My name is %s.' % self.name)
	def __getattr__(self, attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda: 25	#���غ���
		raise AttributeError('\'Student\' object has no attribut \'%s\'' % attr)	#����û�е�����ʱ����ӡ������
print Student('Michael')
s = Student('Michael')
print s
print s.score
print s()
print s.age()	#lambda�ĵ��÷�ʽ
#print s.home	#AttributeError����
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
		
	def __getitem__(self, n):	#Fib��ʼ֧��[]
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):	#�����˶���Ƭ�Ĵ�������
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