# -*- coding: utf-8 -*-
#
#db = {}
import time
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
		lastlogin = loginTime.get(name)
		if lastlogin == None:
			print 'welcome back', name
			print 'first time in four hours.'
		else:
			ltime = time.strptime(loginTime[name])
			ctime = time.strptime(time.ctime())
			if ctime[3] - ltime[3] <= 4:
				print 'You already logged in at %s' % loginTime[name]
				return 3
			else:
				print 'welocme back', name
		loginTime[name] = time.ctime()
	else:
		print 'login incorrect'
def removeuser(user):
	if db.get(user) == None:
		print 'Invalid User'
		return False
	else:
		print 'Remove %s from db' % user
		db.pop(user)
		return True
def readdata(filename):
	db = {}
	datafile = open(filename,'r')
	if datafile:
		for line in datafile.readlines():
			#print line.strip('\n').split(':',1)
			key, value = line.strip('\n').split(':',1)
			db[key] = value
	return db
def savedata(filename,db):
	datafile = open(filename,'w')
	for key in db:
		datafile.writelines('%s:%s\n' % (key, db[key]))
	return True
def show():
	for key in db:
		print key,db[key]
def showmenu():
	prompt = '''
	(N)ew User Login
	(E)xisting User Login
	(S)how User Informations
	(R)emove User
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
			if choice not in 'neqsr':
				print 'invalid option, try again'
			else:
				chosen = True
		if choice == 'n':
			newuser()
		elif choice == 'e':
			olduser()
		elif choice == 's':
			show()
		elif choice == 'r':
			user = raw_input('Enter user name: ')
			removeuser(user)
		else:
			done = True
		
	
if __name__ == '__main__':
	db = readdata('data.txt')
	loginTime = readdata('logintime.txt')
	showmenu()
	#print loginTime
	savedata('data.txt',db)
	savedata('logintime.txt',loginTime)