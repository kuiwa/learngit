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

def print_result(word_in, dic=dictionary, choice=choice_add):
	if choice and search:
		print "%s is alreay in the dic." % word_in
		print "key = %s, value = %s" % (word_in, dic[word_in])
	elif choice == False and search == 'Found':
		print "key = %s, value = %s" % (word_in, dic[word_in])
	elif choice == True and search == False:
		d.add(word_in)
		print "The %s is already added to dic." % word_in
	else:
		print "Sorry, NOT FOUND!"
		
print_result(word_in)

scan_words = raw_input("Please input  words: ")	
if scan_words != '':
	d.scan(scan_words)
else:
	print "Exit!"