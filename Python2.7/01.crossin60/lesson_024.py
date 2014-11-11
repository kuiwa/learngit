def position(x, y):
	if x >= 0:
		if y>= 0:
			print 1
		else:
			print 4
	else:
		if y>= 0:
			print 2
		else:
			print 3
			
print 'Please enter x number:'
x = input()
print 'Please enter y numer:'
y = input()
position(x, y)