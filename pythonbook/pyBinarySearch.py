# -*- coding: utf-8 -*-
# file: pyBinarySearch.py
#
def BinarySearch(l, key):
	low = 0
	high = len(l) - 1
	i = 0
	while ( low <= high ):
		i += 1
		mid = ( low + high ) // 2
		if (l[mid] > key):
			high = mid - 1
		elif (l[mid] < key):
			low = mid + 1
		else:
			print ('use %d time(s)' % i)
			return mid
	return -1
if __name__ == '__main__':
	l = [1, 5, 6, 10, 51, 62, 65, 70]
	print (BinarySearch(l, 1))
	print (BinarySearch(l, 10))
	print (BinarySearch(l, 65))
	print (BinarySearch(l, 70))