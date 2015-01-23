# -*- coding: utf-8 -*-
#
def subchr(string, char, newchar):
	lenS = len(string)
	lenC = len(char)
	if char in string:
		for i in range(lenS-lenC+1):
			if char == string[i:i+lenC]:
				if i == 0:
					return (newchar + string[i+lenC:])
				elif i == lenS-lenC+1:
					return (string[:i] + newchar)
				else:
					return (string[:i] + newchar + string[i+lenC:])
	else:
		return -1
		
if __name__ == '__main__':
	string = "The purpose that two people stay together is not to change the others, but to tolerate and accept the others' faults."
	char = 'fault'
	char = raw_input('char: ')
	newchar = raw_input('newchar: ')
	print subchr(string, char, newchar)
