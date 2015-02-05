# -*- coding: utf-8 -*-
#
import string
def rot13(str):
	lowerString = string.lowercase * 2
	upperString = string.uppercase * 2
	rotString = ''
	for s in str:
		if s in string.lowercase:
			for i in range(len(lowerString)):
				if s == lowerString[i]:
					s = lowerString[i+13]
					break
		elif s in string.uppercase:
			for i in range(len(upperString)):	
				if s == upperString[i]:
					s = upperString[i+13]
					break
		rotString += s
	return rotString
	
if __name__ == '__main__':
	prompt = 'Enter string to rot13: '
	str = raw_input(prompt)
	print 'Your string to en/decrypt was: [%s].' % str
	print 'The rot13 string is:[%s].' % rot13(str)