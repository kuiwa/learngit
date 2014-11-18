# -*- coding: utf-8 -*-

# in or not in
s1 = [1,2,3,4,5,6,7]
s2 = [2,3,6]
s3 = []
for obj in s1:
	if obj not in s2:
		s3.append(obj)
		
print s3

# 连接操作符（+）
print s1 + s2

li = [1,2,3]
li.extend('good')
print li
li = [1,2,3]
li.append('good')
print li

li = [1,2,3]
obj = ['a', 'abc']
li.extend(obj)
print li

li = [1,2,3]
seq = ['a', 'abc']
li.append(seq)
print li

li = ['a','b','c','a','c','a']
print li.index('a')
print li.index('a', 1,len(li)-1)

li = ['a', 'b']
li.insert(1,'Z')
print li

li = ['a','b','c','a','c','a']
li.remove('a')
print li

li = ['a','b']
li.reverse()
print li

li = ['b','c','M',1,'ba']
li.sort()
print li