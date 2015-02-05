# -*- coding: utf-8 -*-
#
db = {}
def newuser():
	prompt = 'login desired: '
	while True:
		name = raw_input(prompt)
		if name in db:
			prompt = 'name taken, try another: '
			continue
		else:
			break
	pwd = raw_input('passwd: ')
	db[name] = pwd
def olduser():
	name = raw_input('login: ')
	pwd = raw_input('Password: ')
	passwd = db.get(name)
	if pwd == passwd:
		print 'welcome back', name
	else:
		print 'login incorrect'
def showmenu():
	prompt = '''
	(N)ew User Login
	(E)xisting User Login
	(Q)uit
	
	Enter choice: '''
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (IndexError,EOFError, KeyboardInterrupt) as e:
				choice = 'q'
			print '\nYou picked: [%s]' % choice
			if choice not in 'neq':
				print 'invalid option, try again'
			else:
				chosen = True
		if choice == 'n':
			newuser()
		elif choice == 'e':
			olduser()
		else:
			done = True
		
	
if __name__ == '__main__':
	showmenu()