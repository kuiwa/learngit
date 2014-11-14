# -*- coding: utf-8 -*-

# for usage
dic = {'name': 'Michael', 'job': 'pythoner', 'age': 32}

for i in dic.items():
	print i

# range()	
for obj in range(5):
	print obj,

print "\n"
	
name = 'BeginMan'
for obj in range(len(name)):
	print '(%d)' % obj, name[obj]
	
for i,j in enumerate(name):
	print i,j

s = [ obj**2 for obj in range(8) if not obj % 2 ]
for i in s:
	print i,