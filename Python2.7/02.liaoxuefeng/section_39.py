#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
	pass
	
s = Student()
s.name = 'Michael'
print s.name

def set_age(self, age):
		self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

def set_score(self, score):
	self.score = score
	
Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
print s.score

class Student2(object):
	__slots__ = ('name', 'age')

s2 = Student2()
s2.name = 'Derek'
s2.age = 25
#s2.score = 99

class GraduateStudent2(Student2):
	pass
g = GraduateStudent2()
g.score = 1000
print g.score