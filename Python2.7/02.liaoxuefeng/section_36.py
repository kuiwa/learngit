#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print 'Animal is running...'
		
class Dog(Animal):
	def run(self):
		print 'Dog is running...'
	def eat(self):
		print 'Eating meat...'
		
class Cat(Animal):
	def run_me(self):
		print 'Cat is running...'



dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()
cat.run_me()

a = list()
b = Animal()
c = Dog()
print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(b, Dog)
print isinstance(c, Dog)
print isinstance(c, Animal)

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())