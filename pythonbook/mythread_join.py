# -*- coding: utf-8 -*-
# file: mythread_join.py
#
import threading
import time
class Mythread(threading.Thread):
	def __init__(self, id):
		threading.Thread.__init__(self)
		self.id = id
	def run(self):
		x = 10
		time.sleep(5)
		print self.id
def func():
	t.start()
	print (t.isAlive())
	for i in range(5):
		print (i)
t = Mythread(2)
func()
def func2():
	t.start()
	print (t.isAlive())
	t.join()
	for i in range(5):
		print(i)
t = Mythread(3)
func2()
t = Mythread(4)
func2()