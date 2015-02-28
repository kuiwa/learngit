#
def multiple(num):
	sum = 0
	for i in range(1,num+1):
		sum += i
	return sum
	
if __name__ == '__main__':
	num = raw_input('Enter a number:> ')
	print multiple(int(num))