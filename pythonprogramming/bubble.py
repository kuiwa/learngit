#
def bubble(a):
	for i in range(len(a)):
		for j in range(len(a)-1):
			if a[j+1] < a[j]:
				a[j+1], a[j] = a[j], a[j+1]
	return a
a = [5, 4, 7, 20, 6, 2, 45, 1, 0]
bubbleA = bubble(a)
print bubbleA