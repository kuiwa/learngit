print '%s is easy to learn' % 'Python'
print "%s's score is %d" % ('Mike', 87)

name = 'Lily'
score = 95
print "%s's score is %d" % (name,score)

name_list = ['Lucy', 'David', 'Tom']
score_list = [95, 96, 97]
i = 0
for x in name_list:
	y = score_list[i]
	i+= 1
	print "%s's score is %d" % (x,y)