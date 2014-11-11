#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
print bart
print Student
jim = Student('', 0)
jim.__init__('Jim', 99)
print jim.name
print jim.score 

bart.name = 'Bart Simpson'
print bart.name
print bart.score
print bart.age

def print_score(std):
	print '%s: %s' % (std.name, std.score)

print_score(bart)
print bart.get_grade()