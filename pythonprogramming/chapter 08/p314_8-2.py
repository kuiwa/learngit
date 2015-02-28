# -*- coding: utf-8 -*-
#
def myRange():
	while True:
		try:
			from_ = int(raw_input('Enter start number: > '))
			to_ = int(raw_input('Enter end number:> '))
			increment_ = int(raw_input('Enter step number:> '))
		except (ValueError) as e:
			print 'error: ' + str(e)
		else:
			for i in range(from_,to_+1,increment_):
				print i,
			break
myRange()