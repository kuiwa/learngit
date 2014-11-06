#!/usr/bin/env python
# -*- coding: utf-8 -*-

#多进程
#multiprocessing
from multiprocessing import Process
import os

#子程序
def run_proc(name):
	print 'Run child process %s (%s)...' % (name, os.getpid())
	
if __name__=='__main__':
	print 'Parent process %s. ' % os.getpid()
	p = Process(target=run_proc, args=('test',))
	print 'Process will start.'
	p.start()
	p.join()
	print 'Process end.'