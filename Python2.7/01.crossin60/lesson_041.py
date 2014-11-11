#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入random函数
from random import choice

#重置已有用户的数据
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
#射门与扑救
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

#用户输入姓名
name = raw_input('Please enter your name:')	
#从game.txt中读取数据
f = open('game.txt')
lines = f.readlines()
f.close()
#建立一个字典用来存储game.txt中的内容
scores = {}
for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]
#用来判断该用户是否在文件中存在，如存在则读取
score_com = scores.get(name)
#如不存在，则将其置为0
if score_com is None:
	score_com = [0, 0, 0]
#如存在，还可以选择是否重置该用户的数据
else: 
	print 'If you want to reset your score_com result, please press 0'
	print 'Else press any other number'
	num_reset = input()
	if num_reset == 0:
		score_com =[0, 0, 0]
	else:
		print 'Read the game.txt!'
print score_com
#定义初始变量
score = [0, 0, 0]
direction = ['left', 'center', 'right']
num = {1: 'left', 2: 'center', 3: 'right'}
j = 0
#1轮5次，如一轮平局则继续下一轮
while(score[0] == score[1]):
	for i in range(5):
		kick()
	j += 5
	score[2] = j
if score[0] > score[1]:
	print 'You Win!'
else:
	print 'You Lose!'
#总的游戏次数
game_times = int(score[2]) + int(score_com[0])
#射门成功次数
shoot_times = int(score[0]) + int(score_com[1])
#扑救成功次数
saved_times = j - int(score[1]) + int(score_com[2]) 
#射门成功率
avg_shoot_times = float(shoot_times) / game_times
#扑救成功率
avg_saved_times = float(saved_times) / game_times
#打印以上数据
print 'You have played %d times.shoot %d times,saved %d times,shoot : saved = %.2f%% : %.2f%%' % (game_times, shoot_times, saved_times, avg_shoot_times, avg_saved_times)
#将本次用户数据放入scores字典中
scores[name] = [str(game_times), str(shoot_times), str(saved_times)]
#初始化一个空字符串变量用来存储所有的数据
result = ''
#以字典的第一个数据位索引，将数据放入result中，并写入文件
for n in scores:
	line = n + ' ' + ' '.join(scores[n]) + '\n'
	result += line
f = open('game.txt', 'w')
f.write(result)
f.close()
