# -*- coding: utf-8 -*-

dict_dir = 'dict.txt'

def add(word,dict_dir):
	word_list = []
	word_list_2 = []
	for w in word.split(":"):
		word_list.append(w)
	s = word_list[0] + ":" + word_list[1]
	file = open(dict_dir, 'a')
	file.write("\n" + s)
	file.close()
	

w = "tt:ss"	
add(w,dict_dir)