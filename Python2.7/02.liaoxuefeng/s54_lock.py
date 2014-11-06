#!/usr/bin/env python
# -*- coding: utf-8 -*-

#�����
import time, threading

#�ٶ�����������д��
balance = 0
lock = threading.Lock()

def change_it(n):
	#�ȴ��ȡ�����Ӧ��Ϊ0
	global balance
	balance = balance + n
	balance = balance - n
	
def run_thread(n):
	for i in range(10000):
		#��Ҫ��ȡ��
		lock.acquire()
		try:
			change_it(n)
		finally:
			#������һ��Ҫ�ͷ���
			lock.release()
			
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance