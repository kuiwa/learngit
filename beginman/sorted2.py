# -*- coding: utf-8 -*-

def result(x):
	dic = {9: 'A', 8: 'B', 7: 'C', 6: 'D'}
	myre = x / 10
	for obj in dic.keys():
		if myre >= obj:
			level = obj
			break
		else:
			level = 'F'
	return dic[level]
	
if __name__ == "__main__":
	score = input("Please enter your score: ")
	print "level: %s" % result(score)