# -*- coding: utf-8 -*-

# dict style
my_stuff = {'apple': "I AM DICT APPLES!"}
print my_stuff['apple']

# module style
import mystuff

mystuff.apple()
print mystuff.tangerine

# class style
class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between."
		
	def apple(self):
		print "I AM CLASSY APPLES!"
	
thing = MyStuff()
print thing.tangerine
thing.apple()