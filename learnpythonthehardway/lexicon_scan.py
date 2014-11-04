# -*- coding: utf-8 -*-
					
class lexicon_dict(object):

	def __init__(self, dict_txt):
		self.dict_txt = dict_txt
	
	def scan(self, words_input):
		value = []
		for w in words_input.split():
			found = False
			dic = self.cat_dict_txt()
			for key in dic:
				if key == w:
					found = True
					break
			if found == True:
				value.append((dic[w], w))
			else:
				value.append(('error',w))
		print value
		

	def cat_dict_txt(self):
		dict_txt = open(self.dict_txt)
		lines = []
		word = []
		for w in dict_txt.readlines():
			strip_dict_txt = []
			for word in w.split(":"):
				strip_dict_txt.append(word.strip())
				lines.append(strip_dict_txt)
		dic = dict(lines)
		dict_txt.close()
		return dic	
		
dict_txt = 'dict.txt'
search = False
d = lexicon_dict(dict_txt)
dictionary = d.cat_dict_txt()

scan_words = raw_input("Please input  words: ")	
if scan_words != '':
	d.scan(scan_words)
else:
	print "Exit!"