f = file('file.txt')
data = f.readline()
print data
f.close()
new = open('new.txt', 'w')
new.write(data)
new.close()