def readdata():
	datafile = open('note.txt','r')
	data = datafile.readlines()
	for i in data:
		print i.strip()
def func():
	for i in range(4):
		if i < 4:
			return i
			
print func()
