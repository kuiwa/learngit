# -*- coding: utf-8 -*-

import string
sen = file("ocr.txt")
s = sen.read()
sen.close()

if __name__ == "__main__":
	r = ''
	for i in s:
		if i in string.letters:
			r += i
	print r