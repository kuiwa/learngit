#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, threading

def worker():
	print 'worker'
	time.sleep(1)
	return

if __name__=='__main__':
	for i in xrange(5):
		t = threading.Thread(target=worker)
		t.start()