# -*- coding: utf-8 -*-
#
" Use list to implenment queue"

queue = []

def enQ():
	queue.append(raw_input('Enter a new queue element: '))
def deQ():
	if len(queue) == 0:
		print "Can't dequeue from empty queue!"
	else:
		print 'Remove [' + queue.pop(0) + ']'
def viewQ():
	print queue

CMDs = { 'e': enQ, 'd': deQ, 'v': viewQ }

def showmenu():
	pr = '''
	(E)nqueue
	(D)equeue
	(V)iew
	(Q)uit
	
	Enter your choice: '''
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (IndexError, KeyboardInterrupt, EOFError) as e:
				print 'Error: ' + str(e)
				choice = 'q'
			if choice not in 'edvq':
				print 'Invalid option, try again!' 
			else:
				print '\nYou Picked [%s]' % choice
				break
		if choice == 'q':
			break
		CMDs[choice]()
		
if __name__ == '__main__':
	showmenu()
