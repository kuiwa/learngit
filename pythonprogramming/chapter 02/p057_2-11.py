# -*- coding: utf-8 -*-
#
def sum(li):
	sumA = 0
	for i in li:
		sumA += i
	return sumA
def ave(li):
	return float(sum(li))/len(li)
def app(li):
	appA = 1
	for i in li:
		appA *= i
	return appA
def max(li):
	maxN = 0
	for i in li:
		if maxN < i:
			maxN = i
	return maxN
print '(1) sum with five numbers'
print '(2) average with five numbers'
print '(3) apply with five numbers'
print '(4) maxinum number'
print '(X) quit'
tag = True
li = [1, 10, 15, 20, 25]
while tag:
	choice = raw_input('Enter your choice: ')
	if choice == '1': print sum(li)
	elif choice == '2': print ave(li)
	elif choice == '3': print app(li)
	elif choice == '4': print max(li)
	elif choice == 'X': tag = False; print 'quit'
	else: print 'Wrong Input!'