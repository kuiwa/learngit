scores = {}
f = open('file.txt')
lines = f.readlines()
for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]
	print scores[s[0]]
score = scores.get('So')
print score