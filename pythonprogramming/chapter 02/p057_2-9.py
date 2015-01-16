#
def sum(x, y):
	return x + y
li = [1, 3, 5, 7, 10]
sumA = 0 
i = 0
while i < len(li):
	sumA = sum(sumA, li[i])
	i += 1
print float(sumA)/len(li)
sumB = 0
for j in li:
	sumB = sum(sumB, j)
print float(sumB)/len(li)
