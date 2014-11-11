try:
	f = file('non-exist.txt')
	print 'File opened!'
	f.close()
except:
	print 'File not exists.'
print 'Done'