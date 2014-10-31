# -*- coding: utf-8 -*-

class lexicon(object):

	def __init__(self, word):
		self.word = word
		
	def print_word(self):
		for split_word in self.word:
			print split_word

	def scan(self, in_word):
		for split_word in self.word:
			if in_word == split_word:
				print in_word
				return in_word
			else:
				print None
				return None
				
class lexicon_dict(object):

	def __init__(self, word):
		self.word = word
		
	def print_word(self):
		for i, split_word_key,split_word_value in enumerate(self.word):
			print split_word_key
			print split_word_value

	def scan(self, in_word):
		split_word = []
		for i, split_word in enumerate(self.word):
			print i
			print split_word		
		
dictionary = {'verb': 'go', 'verb': 'stop'}
verbs = ['go', 'stop', 'kill', 'eat']
v = lexicon(verbs)
v.print_word()
v.scan('go')

d = lexicon_dict(dictionary)
d.scan('go')