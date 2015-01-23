# -*- coding: utf-8 -*-
#
" 石头剪刀布 "
import random
def game(me):
	computer = random.choice(['paper', 'rock', 'scissor'])
	aDict = {'paper':1, 'scissor':2, 'rock': 3}
	if me == computer:
		print 'Duce, %s vs %s' % (me, computer)
	elif (aDict[me] - aDict[computer]) in (1, -2):
		print 'You win, %s vs %s' % (me, computer)
	else:
		print 'You lose, %s vs %s' % (me, computer)
def gameB(me):
	computer = random.randrange(1,4)
	dict1 = {'paper':'1', 'scissor':'2', 'rock':'3'}
	dict2 = {'12':'lose', '23':'lose', '31':'lose', '21': 'win', '32': 'win', '13': 'win', '11': 'Duce', '22':'Duce', '33':'Duce' }
	return dict2[dict1[me] + str(computer)]
if __name__ == '__main__':
	pr = '''
	(1) paper
	(2) rock
	(3) scissor
	Please enter your choice: 
	'''
	while True:
		try:
			me = raw_input(pr)
			game(me)
			print gameB(me)
		except KeyError as e:
			print 'Error: ' + str(e)
		else:
			break
