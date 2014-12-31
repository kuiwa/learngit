# -*- coding: utf-8 -*-
# try_except.py
#
l = [1, 2, 3]
print '**********1***********'
try:
	l[5]/0
except:
	print 'Error'
else:
	print 'No Error'
print '**********2***********'	
try:
	print l[5]
except IndexError as Error:
	print Error
else:
	print 'No Error'
print '**********3***********'	
try:
	l[2]/0
except (IndexError,ZeroDivisionError):
	print 'Error'
else:
	print 'No Error'
print '**********4***********'
try:
	l[2]/0
except (IndexError,ZeroDivisionError) as value:
	print value
else:
	print 'No Error'
print '**********5***********'	
try:
	l[5]/0
except IndexError as error:
	print error
except ZeroDivisionError as error:
	print error
else: 
	print 'No Error'