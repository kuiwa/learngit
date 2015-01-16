# -*- coding: utf-8 -*-
#
"Use dict to do 5-3"
def grade(score):
	list_grade = {0:'F', 1:'F', 2:'F', 3:'F', 4:'F', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}
	return list_grade[score//10]
if __name__ == '__main__':
	while True:
		score = raw_input('Enter your score: >')
		try:
			scoreInt = int(score)
		except ValueError as e:
			print 'Error: ' + str(e)
		else:
			if 0 <= scoreInt <= 100:
				print grade(scoreInt)
				break
			else:
				print "Wrong score number!"