# -*- coding: utf-8 -*-

db = {}

def newuser():
	prompt = "login desired: "
	while True:
		name = raw_input(prompt).strip()
		if name == '':
			prompt = "Invalid input, try again!\nlogin desired: "
			continue
		if db.has_key(name):
			prompt = "name taken, try another!\nlogin desired: "
			continue
		else:
			break
	pwd = raw_input("Password: ").strip()
	db[name] = pwd
	
def olduser():
	name = raw_input("name: ")
	pwd = raw_input("password: ")
	if db.get(name) == pwd:
		print "welcome back, ", name
	else:
		print "login Error"
	
def showmenu():
	prompt = '''
	*************************
	Welcome to Python System!
	-------------------------
	|(N)ew User Login        |
	|(L)ogin your system     |
	|(Q)uit                  |
	|(P)rint db              |
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
			print "\nYou picked:[%s]" % choice
			if choice not in 'qnlp':
				print "Invalid option, try again!"
			else:
				chosen = True
		if choice == 'q': done = True
		if choice == 'n': newuser()
		if choice == 'l': olduser()
		if choice == 'p': print db
		
if __name__ == "__main__":
	showmenu()