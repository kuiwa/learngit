# -*- coding: utf-8 -*-
#
def tr(srcstr, dststr, string):
	if srcstr not in string:
		print 'srcstr is not included in string.'
		return False
	lenA = len(srcstr)
	lenB = len(string)
	i = 0
	while i <= lenB-lenA:
	#for i in range(lenB-lenA):
		if srcstr.lower() == string[i:i+lenA].lower():
			string = string[:i] + dststr + string[i+lenA:]
		i += 1
			#break
	
	return string
	
if __name__ == '__main__':
	print tr('abc','mno','abcdefAbc')
