#!/usr/bin/env python
# -*- coding: utf-8 -*-

#���ؼ̳У��ܰ��Ĺ���
class Animal(object):	#������
	pass
	
class Mammal(Animal):	#���鶯����
	pass
	
class Bird(Animal):		#����
	pass
	
class RunnableMixin(object):	#½��
	def run(self):
		print('Running...')
		
class FlyableMixin(object):		#����
	def fly(self):
		print('Flying...')

class CarnivorousMixin(object):	#ʳ��
	def eat(self):
		print('Eat meal...')
		
class HerbivoresMixin(object):	#ʳ��
	def eat(self):
		print('Eat vegetable...')
		
class Dog(Mammal, RunnableMixin, CarnivorousMixin):				#��
	pass
	
class Bat(Mammal, FlyableMixin, CarnivorousMixin):			#����
	pass
	
class Parrot(Bird, FlyableMixin, HerbivoresMixin):			#����
	pass
	
class Ostrich(Bird, RunnableMixin, HerbivoresMixin):		#����
	pass
	
d = Dog()
d.run()
d.eat()