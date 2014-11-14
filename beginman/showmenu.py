# -*- coding: utf-8 -*-

# http://www.cnblogs.com/BeginMan/archive/2013/03/14/2958985.html
def showmenu():
	prompt = '''
	*************************
	Welcome to Python System!
	-------------------------
	|(N)ew User Login        |
	|(L)ogin your system     |
	|(Q)uit                  |
	-------------------------
	Enter Choice:
	*************************
	'''
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except(IndexError, EOFError, KeyboardInterrupt):
				choice = 'q'
			print '\n You picked:[%s]' % choice
			if choice not in 'nlq':
				print 'Invalid option, try again'
			else:
				chosen = True
		if choice == 'q': done = True
		if choice == 'n': print "newUser()"
		if choice == 'l': print "oldUser()"
		
# main
if __name__ == "__main__":
	showmenu()