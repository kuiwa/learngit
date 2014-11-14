# -*- coding: utf-8 -*-

'''
1 >>> help(zip)
2 Help on built-in function zip in module __builtin__:
3 
4 zip(...)
5     zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
6     
7     Return a list of tuples, where each tuple contains the i-th element
8     from each of the argument sequences.  The returned list is truncated
9     in length to the length of the shortest argument sequence.
'''

name = ('jack', 'Michael', 'Peter', 'Joe')
age = (30, 25, 20, 40)
for n, a in zip(name, age):
	print n,a

print "------------"	
all = {'jack': 30, 'Michael': 25, 'Peter': 20, 'Joe': 40}
for n in all.keys():
	print n, all[n]
	
z1 = [1, 2, 3]
z2 = [4, 5, 6]
result = zip(z1, z2)
print result

z3 = [4, 5, 6, 7]
result = zip(z1, z3)
print result

# zip()配合*号操作符，可以将已经zip过的列表对象解压
print zip(*result)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [row[0] for row in a]
print [[row[col] for row in a] for col in range(len(a[0]))]

print zip(*a)
print map(list, zip(*a))

x = [1, 2, 3]
y = ['a', 'b', 'c']
print zip(*zip(x, y))