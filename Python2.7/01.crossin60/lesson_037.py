key1 = 'a'
key2 = 202
key3 = 'James'
value1 = 1
value2 = 2
value3 = 007
d = {key1 : value1, key2 : value2 , key3 : value3}
print d
print d['a']
print d[202]

for key in d:
	print d[key]
	
d[202] = 202
print d
d['Conan'] = 71
print d
del d['a']
print d

for key in d:
	print key, d[key]