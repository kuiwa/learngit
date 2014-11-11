#!/usr/bin/env python
# -*- coding: utf-8 -*-

#����random����
from random import choice

#���������û�������
def reset_score():
	print 'If you want to reset your score_com result, please press 0'
	print 'Else press any other number'
	num_reset = input()
	if num_reset == 0:
		print 'Reset the game.txt!'
		f = open('game.txt', 'w')
		f.write('player 0 0 0')
		f.close()
	else:
		print 'Read the game.txt!'
#�������˾�
def kick():
	print '==== Round %d ====' % (i+1+j)
	print '==== You Kick! ===='
	print 'Choose one side for shoot:'
	print '1.left	 2.center    3.right'
	your_num = input()
	you = num[your_num]
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
	print '1.left	 2.center    3.right'
	your_num = input()
	you = num[your_num]
	print 'You saved ' + you
	com = choice(direction)
	print 'Computer kicked ' + com
	if you == com:
		print 'Saved!'
	else:
		print 'Oops...'
		score[1] += 1
	print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])		

#�û���������
name = raw_input('Please enter your name:')	
#��game.txt�ж�ȡ����
f = open('game.txt')
lines = f.readlines()
f.close()
#����һ���ֵ������洢game.txt�е�����
scores = {}
for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]
#�����жϸ��û��Ƿ����ļ��д��ڣ���������ȡ
score_com = scores.get(name)
#�粻���ڣ�������Ϊ0
if score_com is None:
	score_com = [0, 0, 0]
#����ڣ�������ѡ���Ƿ����ø��û�������
else: 
	print 'If you want to reset your score_com result, please press 0'
	print 'Else press any other number'
	num_reset = input()
	if num_reset == 0:
		score_com =[0, 0, 0]
	else:
		print 'Read the game.txt!'
print score_com
#�����ʼ����
score = [0, 0, 0]
direction = ['left', 'center', 'right']
num = {1: 'left', 2: 'center', 3: 'right'}
j = 0
#1��5�Σ���һ��ƽ���������һ��
while(score[0] == score[1]):
	for i in range(5):
		kick()
	j += 5
	score[2] = j
if score[0] > score[1]:
	print 'You Win!'
else:
	print 'You Lose!'
#�ܵ���Ϸ����
game_times = int(score[2]) + int(score_com[0])
#���ųɹ�����
shoot_times = int(score[0]) + int(score_com[1])
#�˾ȳɹ�����
saved_times = j - int(score[1]) + int(score_com[2]) 
#���ųɹ���
avg_shoot_times = float(shoot_times) / game_times
#�˾ȳɹ���
avg_saved_times = float(saved_times) / game_times
#��ӡ��������
print 'You have played %d times.shoot %d times,saved %d times,shoot : saved = %.2f%% : %.2f%%' % (game_times, shoot_times, saved_times, avg_shoot_times, avg_saved_times)
#�������û����ݷ���scores�ֵ���
scores[name] = [str(game_times), str(shoot_times), str(saved_times)]
#��ʼ��һ�����ַ������������洢���е�����
result = ''
#���ֵ�ĵ�һ������λ�����������ݷ���result�У���д���ļ�
for n in scores:
	line = n + ' ' + ' '.join(scores[n]) + '\n'
	result += line
f = open('game.txt', 'w')
f.write(result)
f.close()
