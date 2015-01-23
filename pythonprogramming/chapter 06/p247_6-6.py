# -*- coding: utf-8 -*-
#
" this function can replace string.strip()"
def new_strip(strInput):
	for i in range(len(strInput)):
		if strInput[i] != ' ':
			break
	start = i
	i = len(strInput)
	for j in strInput[::-1]:
		i -= 1
		if j != ' ':
			break
	stop = i + 1
	return strInput[start:stop]

if __name__ == '__main__':
	strInput = raw_input('Enter a string: >')
	print new_strip(strInput)
