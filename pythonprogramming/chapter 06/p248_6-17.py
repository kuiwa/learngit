#
" refer pop() to design mypop()"
def mypop(aList):
	if len(aList) == 0:
		print 'empty list can not pop()'
		return None
	last = aList[-1]
	del aList[-1]
	return last

if __name__ == '__main__':
	aList = ['Life', 'end', 'when', 'you', 'stop', 'dreaming']
	for i in range(len(aList)+1):
		print mypop(aList)
