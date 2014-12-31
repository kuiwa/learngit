# -*- coding: utf-8 -*-
# file: try_except_assert.py
#
l = []
try:
	assert len[l], 'Error'
except:
	print 'assert error'
else:
	print 'No Error'
l.append(1)
assert len(l)