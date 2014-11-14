# -*- coding: utf-8 -*-

def result(x):
	dic = {9: 'A', 8: 'B', 7: 'C', 6: 'D'}
	myre = x / 10
	# sorted按照key的降序来排列dic
	for obj in sorted(dic.keys(), reverse = True):
		# 只要大于9即为A，如超过100也是A
		if myre >= obj:
			out = dic[obj]
			break
		else:
			out = 'F'
	return out
	
if __name__ == "__main__":
	score = input("Enter your score: ")
	print 'level: %s' % result(score)