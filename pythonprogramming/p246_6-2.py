# -*- coding: utf-8 -*-
#
" head with letters or '_', others with alphanumeric"
import string
import keyword
def ifVliad(alph,first=True)
	alphas = string.letters + '_'
	nums = string.digits
	alphnums = alphas + nums
	if first:
		if alph not in alphas:
			print 'invalid: first symbol must be alphabetic'
			return False
	else:
		if alph not in alphnums:
			print ''invalid: remaining symbols must be alphanumeric'
def keywords(myInput):
	if myInput in keywor.kelist:
		return True
	else:
		return False

break_id = True
print 'Welcome to the Identifier Checker v2.0'
while break_id:
	myInput = raw_input('Identifier to test? ')
	length = len(myInput)
	if length == 0:
		print 'Testees must be at least 1 chars long.'
	elif length >= 1:
		if myInput[0] not in alphas:

		else:
			if length > 1:
				right = True
			
				for otherChar in myInput[1:]:
					if otherChar not in alphnums:
						
					right = False
					break
				if right == True:
					print 'okay as an identifier'

