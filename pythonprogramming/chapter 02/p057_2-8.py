#
def sum(x, y):
	return x + y
data = input('Enter your number and it will be add with li: ')
li = [1, 2, 3, 4, 5]
li.append(data)
i = 0
sumA = 0
while i < len(li):
	sumA = sum(li[i], sumA)
	i += 1
print sumA

sumB = 0
for j in li:
	sumB = sum(j, sumB)
print sumB