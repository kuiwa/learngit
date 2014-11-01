# -*- coding: utf-8 -*-
					
class lexicon_dict(object):

	def __init__(self, dict_txt):
		self.dict_txt = dict_txt
	
	# useless
	def print_dict_txt(self):
		for i, split_dict_txt_key,split_dict_txt_value in enumerate(self.dict_txt):
			print split_dict_txt_key
			print split_dict_txt_value
	
	# useless
	def scan(self, in_dict_txt):
		split_dict_txt = []
		for i, split_dict_txt in enumerate(self.dict_txt):
			print i
			print split_dict_txt		

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
		
	def add(self, word):
		word_list = []
		word_list_2 = []
		for w in word.split(":"):
			word_list.append(w)
		s = word_list[0] + ":" + word_list[1]
		file = open(self.dict_txt, 'a')
		file.write("\n" + s)
		file.close()		

dict_txt = 'dict.txt'
search = False
d = lexicon_dict(dict_txt)
dictionary = d.cat_dict_txt()


print """
	Please enter 'yes' if you want to add word into the dictionary.
	Otherwise HIT RETURN.
	"""
choice = raw_input("> ")
print "Enter a word :"
print "Such as: take: verb"
word_in = raw_input(">")

if choice == 'yes':
	choice_add = True
else:
	choice_add = False

for key in dictionary:
	if word_in == key:
		search = 'Found'
		break

if choice_add and search:
	print "%s is alreay in the dictionary." % word_in
	print "key = %s, value = %s" % (word_in, dictionary[word_in])
elif choice_add == False and search == 'Found':
	print "key = %s, value = %s" % (word_in, dictionary[word_in])
elif choice_add == True and search == False:
	d.add(word_in)
	print "The %s is already added to dictionary." % word_in
else:
	print "Sorry, NOT FOUND!"