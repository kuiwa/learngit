# -*- coding: utf-8 -*-
#
" head with letters or '_', others with alphanumeric"
import string
import keyword
def isValid(alph,first=True):
	alphas = string.letters + '_'
	nums = string.digits
	alphnums = alphas + nums
	if first:
		if alph not in alphas:
			print 'invalid: first symbol must be alphabetic'
			return False
	else:
		for i in alph:
			if i not in alphnums:
				print 'invalid: remaining symbols must be alphanumeric'
				return False
	return True
def keywords(myInput):
	if myInput in keyword.kwlist:
		return True
	else:
		return False

print 'Welcome to the Identifier Checker v2.0'
while True:
	myInput = raw_input('Identifier to test? ')
	length = len(myInput)
	if length == 0:
		print 'Testees must be at least 1 chars long.'
		continue
	elif length == 1:
		ident = isValid(myInput[0])
	else:
		ident = isValid(myInput[0])
		ident = ident & isValid(myInput[1:],first=False)
	if ident:
		print 'okay as an identifier'
		if keywords(myInput):
			print "It's a keyword"
		else:
			print "It's not a keyword"
		break
