# -*- coding: utf-8 -*-
#
" head with letters or '_', others with alphanumeric"
import string

alphas = string.letters + '_'
nums = string.digits
break_id = True

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')
length = len(myInput)
if length > 1:
	if myInput[0] not in alphas:
		print 'invalid: first symbol must be alphabetic'
	else:
		alphnums = alphas + nums
		right = True
		for otherChar in myInput[1:]:
			if otherChar not in alphnums:
				print 'invalid: remaining symbols must be alphanumeric'
				right = False
				break
		if right == True:
			print 'okay as an identifier'
