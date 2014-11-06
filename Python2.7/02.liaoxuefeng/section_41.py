#!/usr/bin/env python
# -*- coding: utf-8 -*-

#多重继承，很棒的功能
class Animal(object):	#动物类
	pass
	
class Mammal(Animal):	#哺乳动物类
	pass
	
class Bird(Animal):		#鸟类
	pass
	
class RunnableMixin(object):	#陆行
	def run(self):
		print('Running...')
		
class FlyableMixin(object):		#飞行
	def fly(self):
		print('Flying...')

class CarnivorousMixin(object):	#食肉
	def eat(self):
		print('Eat meal...')
		
class HerbivoresMixin(object):	#食草
	def eat(self):
		print('Eat vegetable...')
		
class Dog(Mammal, RunnableMixin, CarnivorousMixin):				#狗
	pass
	
class Bat(Mammal, FlyableMixin, CarnivorousMixin):			#蝙蝠
	pass
	
class Parrot(Bird, FlyableMixin, HerbivoresMixin):			#鹦鹉
	pass
	
class Ostrich(Bird, RunnableMixin, HerbivoresMixin):		#鸵鸟
	pass
	
d = Dog()
d.run()
d.eat()