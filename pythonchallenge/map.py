# -*- coding: utf-8 -*-

letters = 'abcdefghijklmnopqrstuvwxyz'
letters_right2 = 'cdefghijklmnopqrstuvwxyzab'

letter_dic = {}
for i in range(26):
	letter_dic[letters[i]] = letters_right2[i]

#print letter_dic
sentence = open("map.txt")
sen = sentence.read()
for word in sen:
	for letter in word:
		if letter_dic.has_key(letter):
			print letter_dic[letter],
		else:
			print letter,

print ''
for answer in 'map':
	print letter_dic[answer],