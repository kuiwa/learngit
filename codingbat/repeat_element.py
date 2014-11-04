# -*- coding: utf-8 -*-

A = ['a','b','e','d','e','a','bb','bb']
def repeat_element(list):
	count = 0
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			if A[i] == A[j]:
				count += 1
	return count
	
print repeat_element(A)