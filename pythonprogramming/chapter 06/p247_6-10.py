#
import string
def tranStr(s):
	s2 = ''
	for i in s:
		if i in string.lowercase:
			i = i.upper()
		elif i in string.uppercase:
			i = i.lower()
		s2 += i
	return s2
def tranStrB(s):
	aList = list(s)
	for i in range(len(aList)):
		if aList[i] in string.lowercase:
			aList[i] = aList[i].upper()
		elif aList[i] in string.uppercase:
			aList[i] = aList[i].lower()
	return "".join(aList)
s = raw_input('Enter a string: >')
print tranStr(s)
print tranStrB(s)
