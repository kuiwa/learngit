#

def div(a, b):
	if a % b == 0 or b % a == 0:
		return True
	else:
		return False
while True:
	print 'Enter two number:'
	a = raw_input('First one: >')
	b = raw_input('Second one: >')
	try:
		aInt = int(a)
		bInt = int(b)
	except ValueError as e:
		print 'Error: ' + str(e)
	else:
		print div(aInt, bInt)
		break