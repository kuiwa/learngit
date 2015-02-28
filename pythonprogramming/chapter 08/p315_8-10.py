# -*- coding: utf-8 -*-
#
def count(sen, style='vowel'):
	if style == 'word':
		num = len(list(sen.strip().split()))
		return num
	elif style == 'consonant':
		seq = 'bcdfghjklmnpqrstvwxyz'
	else :
		seq = 'aeiou'
	num = 0
	for w in sen:
		for i in w:
			if i in seq:
				num += 1
	return num
sentence = 'Life brings tears, smiles and memories. The tears will dry, the smiles will fade, while the memories last forever'	
print count(sentence)
print count(sentence,'consonant')
print count(sentence,'word')
