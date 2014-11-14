# -*- coding: utf-8 -*-

db = {}
def newuser():
	prompt = "login desired: "
	while True:
		name = raw_input(prompt).strip()
		if name == "":
			print "Invalid input, try again."
			continue
		if db.has_key(name):
			print "name taken, try another."
			continue
		else:
			break
	pwd = raw_input("Password: ").strip()
	db[name] = pwd

def olduser():
	name = raw_input("login name: ").strip()
	if db.has_key(name):
		pwd = raw_input("Password: ").strip()
		if db[name] == pwd:
			print "welcome back, ", name
		else:
			print "login error"
	else:
		print "login name not exists"
def showmenu():
	prompt = '''
	************************
	Welcome to Python System
	 -----------------------
	|(N)ew User Login       |
	|(L)ogin your system    |
	|(Q)uit                 |
	|(P)rint User Db        |
	 -----------------------
	Enter Choice:
	************************
	
	'''
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except(IndexError, EOFError):
				choice = 'q'
			if choice not in 'nlqp':
				print "Invalid choice, try again."
			chosen = True
		if choice == 'n': newuser()
		if choice == 'l': olduser()
		if choice == 'q': done = True
		if choice == 'p': print db

if __name__ == "__main__":
	showmenu()