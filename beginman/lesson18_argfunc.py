# -*- coding: utf-8 -*-

def foo():
	print 'foo'
	
def bar(argfunc):
	print 'in bar()'
	argfunc()

if __name__ == "__main__":	
	bar(foo)