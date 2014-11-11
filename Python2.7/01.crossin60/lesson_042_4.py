print 'Please enter your name:'
name = raw_input()	
#def if_exist(name):
f = open('game.txt')
lines = f.readlines()
scores = {}
for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]
score_com = scores.get(name)
if score_com is None:
	score_com = [0, 0, 0]
print score_com
f.close()
#score_com = scores[name].split()


scores = {'Derek': '0 1 2', 'Mike': '1 2 3'}
scores['Nike'] = '2 3 4'
print scores
result = ''
for n in scores:
	line = n + ' ' + ' '.join(scores[n]) + '\n'
	result += line
f = open('game.txt', 'w')
f.write(result)
f.close()
