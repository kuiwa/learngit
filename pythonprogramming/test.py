#
import string

alphas = string.letters + '_'
nums = string.digits
alphnums = alphas + nums
t = raw_input('Enter: ')
c = True
for i in t:
	if i not in alphnums:
		print 'Invalid'
		c = False
		break
if c == True:
	print 'Right'
