#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
		
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
			
	def get_name(self):
		return self.__name
	
	def get_score(self):
		return self.__score
		
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)
		
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
print bart
print Student
jim = Student('', 0)
jim.__init__('Jim', 99)
print jim.get_name()
print jim.get_score()
jim_score = raw_input("Please enter Jim's score: ")
jim.set_score(int(jim_score))
jim.print_score()
