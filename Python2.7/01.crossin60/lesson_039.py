from random import choice

f = open('game.txt')
score_sum = f.read().split()
score = [0, 0, 0]
direction = ['left', 'center', 'right']
num = {1: 'left', 2: 'center', 3: 'right'}

def kick():
	print '==== You Kick! ===='
	print 'Choose one side for shoot:'
	#print 'left, center, right'
	print '1.left	 2.center    3.right'
	#you = raw_input()
	your_num = input()
	you = num[your_num]
	print 'You kicked ' + you
	#print you

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
		kick()
	j += 5
	score[2] = j
if score[0] > score[1]:
	print 'You Win!'
else:
	print 'You Lose!'
game_times = int(score[2]) + int(score_sum[0])
shoot_times = int(score[0]) + int(score_sum[1])
saved_times = j - int(score[1]) + int(score_sum[1]) 
avg_shoot_times = float(shoot_times) / game_times
avg_saved_times = float(saved_times) / game_times
print 'You have played %d times, shoot %d times, saved %d times, shoot : saved = %.2f%% : %.2f%%' % (game_times, shoot_times, saved_times, avg_shoot_times, avg_saved_times)

