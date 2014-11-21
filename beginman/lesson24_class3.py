# -*- coding: utf-8 -*-

class Test():
	myVersion="1.0"
	
t = Test()
print Test.myVersion
print t.myVersion
Test.myVersion = "2.0"
print Test.myVersion
print t.myVersion
t.myVersion = "3.0"
print Test.myVersion
print t.myVersion
Test.myVersion = "4.0"
print Test.myVersion
print t.myVersion
del t.myVersion
print t.myVersion

Test.x = {'myVersion':'1.0'}
print Test.x
print t.x
t.x['myVersion'] = '2.0'
print t.x
print Test.x