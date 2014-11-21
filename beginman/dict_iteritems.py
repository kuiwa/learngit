# -*- coding: utf-8 -*-

dic = {'a':31, 'bc':5, 'c':3, 'dd':4, '33':53, 'd':0}

print sorted(dic.iteritems(), key=lambda d:d[1], reverse = False)
print sorted(dic.items(), key = lambda d:d[0], reverse = True)
print dic.iteritems
print dic.items

for obj in dic.iteritems():
	print obj,obj[0],obj[1]

for obj in dic.items():
	print obj,obj[0],obj[1]
