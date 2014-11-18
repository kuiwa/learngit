# -*- coding: utf-8 -*-

li = ['a','b','c','a']
se = set(li)
print se

s = set('beginman')
print s
t = frozenset('beginman')
print t

print 'a' in s
print 'n' in s
for i in s:
	print i,

print ''

t1 = set(t)
print t1
t1.add(0)
t1.update('MM')
t1.remove('b')
print t1

s1 = set('phon')
s2 = set('nics')
s3 = s1 | s2
print s3
print s1.union(s2)

print s1&s2
print s1.intersection(s2)
print s1-s2
print s1.difference(s2)
print s1^s2
print s1.symmetric_difference(s2)
print s1 and s2
print s1 or s2