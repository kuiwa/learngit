# -*- coding: utf-8 -*-
#
def rfindchr(string, char):
	lenS = len(string)
	lenC = len(char)
	if char in string:
		for i in range(lenS-lenC)[::-1]:
			if char == string[i:i+lenC]:
				return i
	else:
		return -1
		
if __name__ == '__main__':
	string = "The purpose that two people stay together is not to change the others, but to tolerate and accept the others' faults"
	char = 'fault'
	char = raw_input()
	print rfindchr(string, char)
