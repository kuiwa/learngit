# -*- coding: utf-8 -*-
# file: mythread_name.py
#
import threading
class mythread(threading.Thread):
	def __init__(self, threadname):
		threading.Thread.__init__(self, name=threadname)
	def run(self):
		print (self.getName())
t1 = mythread('t1')
print t1.getName()
t1.setName('T')
print t1.getName()