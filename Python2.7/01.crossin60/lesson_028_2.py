from random import choice

score = [0, 0, 0]
direction = ['left', 'center', 'right']

def kick():
	print '==== You Kick! ===='
	print 'Choose one side for shoot:'
	print 'left, center, right'
	you = raw_input()
	print 'You kicked ' + you
	com = choice(direction)
	print 'Computer saved ' + com
	if you != com:
		print 'Goal!'
		score[0] += 1
	else:
		print 'Oops...'
	print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])
	
	print '==== You saved! ===='
	print 'Choose one side to save:'
	print 'left, center, right'
	you = raw_input()
	print 'You saved ' + you
	com = choice(direction)
	print 'Computer saved ' + com
	if you == com:
		print 'Saved!'
	else:
		print 'Oops...'
		score[1] += 1
	print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])

j = 0
while(score[0] == score[1]):
	for i in range(5):
		print '==== Round %d ====' % (i+1+j)
		score[2] = 1 + j
		kick()
	j += 5
if score[0] > score[1]:
	print 'You Win!'
else:
	print 'You Lose!'
