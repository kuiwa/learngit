# -*- coding: utf-8 -*-

import re

sen = file("equality.txt")
s = sen.read()
sen.close()

if __name__ == "__main__":
	string = ''
	for i in xrange(3,len(s)-3):
		if re.match(r'(\A[A-Z]{3})([a-z])([A-Z]{3}\Z)',s[i-3:i+4]):
			if ((i-3 != 0) and (i+4 != len(s))) :
				if re.match(r'([a-z])', s[i-4]) :
					if re.match(r'([a-z])', s[i+4]):
						string += s[i]
	print string