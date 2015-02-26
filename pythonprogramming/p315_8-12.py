# -*- coding: utf-8 -*-
#
def changeNum(min,max):
	print 'Enter begin value: %s' % min
	print 'Enter end value: %s' % max
	print 'DEC	BIN	OCT	HEX	ASCII'
	print '-' * 40
	for i in range(min, max+1):
		print '%3d  %9s  %3s  %3s' % (i, bin(i), oct(i), hex(i)),
		if i in range(256):
			print chr(i)
		else:
			print 
		
if __name__ == '__main__':
	changeNum(0,300)