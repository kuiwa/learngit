# -*- coding: utf-8 -*-
#
def sortDict(aDict):
	# sorted by value
	print sorted(aDict.iteritems(), key=lambda d:d[1], reverse=False)
	# sorted by key
	print sorted(aDict.iteritems(), key=lambda d:d[0], reverse=False)
	
if __name__ == '__main__':
	aDict = { 'James':1, 'Sarah':2, 'Jack':3, 'Nina':4, 'Meilin':5, 'Modor':6}
	print aDict
	sortDict(aDict)