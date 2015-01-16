# -*- coding: utf-8 -*-
#
" head with letters or '_', others with alphanumeric"
import string

alphas = string.letters + '_'
nums = string.digits
break_id = True
while break_id:
	print 'Welcome to the Identifier Checker v1.0'
	print 'Testees must be at least 2 chars long.'
	myInput = raw_input('Identifier to test? ')
	length = len(myInput)
	if length > 1:
		if myInput[0] not in alphas:
			print 'invalid: first symbol must be alphabetic'
		else:
			alphnums = alphas + nums
			for otherChar in myInput[1:]:
				if otherChar not in alphnums:
					print '''invalid: remaining
					symbols must be alphanumeric'''
				else:
					print 'okay as an identifier'
					break_id = False
					break
	else:
		print 'identifier length must be greater than 2'