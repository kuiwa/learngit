# -*- coding: utf-8 -*-
#
import random
def setRand():
	s = set()
	for t in range(random.randint(0,9)):
		randN = random.randint(0,9)
		s.add(randN)
	return s
if __name__ == '__main__':
	setA = setRand()
	setB = setRand()
	print setA | setB
	print setA & setB