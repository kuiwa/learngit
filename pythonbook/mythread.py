# -*- coding: utf-8 -*-
# file: mythread.py
#
import threading
import time
class mythread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num
	def run(self):
		print 'I am ', self.num
t1 = mythread(1)
t2 = mythread(2)
t3 = mythread(3)
t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()