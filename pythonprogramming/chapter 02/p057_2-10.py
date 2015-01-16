#
def converage(x):
	if x <= 100 and x >= 1: return False
	else: return True
tag = True
while tag:
	data = raw_input('Enter a number 1-100: ')
	try:
		tag = converage(int(data))
	except ValueError as valueerr:
		print 'Error: ' + str(valueerr)
print 'Successfully!'