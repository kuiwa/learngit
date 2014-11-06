#!/usr/bin/env python
# -*- coding: utf-8 -*-

#�����
#multiprocessing: Queue,Pipes
from multiprocessing import Process, Queue
import os, time, random

#д���ݽ���ִ�еĴ���
def write(q):
	for value in ['A', 'B', 'C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())
		
#�����ݽ���ִ�еĴ���
def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue.' % value
		
if __name__=='__main__':
	#�����̴���Queue�����������ӽ���
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	#�����ӽ���pw��д��
	pw.start()
	#�����ӽ���pr����ȡ
	pr.start()
	#�ȴ�pw����
	pw.join()#pr����������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ
	pr.terminate()