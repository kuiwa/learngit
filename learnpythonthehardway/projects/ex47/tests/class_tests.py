# -*- coding: utf-8 -*-

from nose.tools import *
class testRoom(object):
	
	def setUp(self):
		print "SETUP!"
		
	def tearDown(self):
		print "TEAR DOWN!"
		
	def test_Basic(self):
		print "test_basic()"