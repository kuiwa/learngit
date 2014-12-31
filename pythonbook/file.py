# -*- coding: utf-8 -*-

file = open('python.txt','w')
file.write('python\n')

a = []
for i in range(10):
	s = str(i) + '\n'
	a.append(s)
file.writelines(a)
file.close()
file = open('python.txt','r')
s = file.read()
print (s)
file.close()
file = open('python.txt','r')
l = file.readlines()
print (l)
file.close()