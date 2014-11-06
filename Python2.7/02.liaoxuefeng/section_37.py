#!/usr/bin/env python
# -*- coding: utf-8 -*-

print type(123)
print type('str')
print type(None)

import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(int) == type(str) == types.TypeType
print isinstance('a', str)
print isinstance(u'a', unicode)
print isinstance(123, int)

class Animal(object):
	pass
class Dog(Animal):
	pass
class Husky(Dog):
	pass
a = Animal
d = Dog()
h = Husky()

print isinstance(Husky, Dog)
print isinstance(h, Husky)
print isinstance(h, Dog)

print dir('ABC')
print len('ABC')
print 'ABC'.__len__()

class MyObject(object):
    def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
		
obj = MyObject()
print hasattr(obj, 'x')
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print hasattr(obj, 'power')
fn = getattr(obj, 'power')
print fn
print fn()
#print obj.x