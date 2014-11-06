f = file('scores.txt')
lines = f.readlines()
print lines
f.close()

results = []
for line in lines:
	print line
	data = line.split()
	print data
	
	sum = 0

	for score in data[1:]:
		point = int(score)
		if point < 60:
			continue
		sum += int(score)
	result = '%s\t:%d\n' % (data[0], sum)
	print result
	results.append(result)
#print results
output = file('result.txt', 'w')
output.writelines(results)
output.close()