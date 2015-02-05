# -*- coding: utf-8 -*-
#
def reverseDict(aDict):
	bDict = {}
	for key in aDict:
		bDict[aDict[key]] = key
	return bDict
	
if __name__ == '__main__':
	aDict = {'this':1, 'will':2, 'be':3, 'a':4, 'better':5, 'day':6}
	print reverseDict(aDict)