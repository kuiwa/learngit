#!/usr/bin/env python
# -*- coding: utf-8 -*-

#单元测试

import unittest

from s47_mydict import Dict

class TestDict(unittest.TestCase):
#定义测试单元的类
	def setUp(self):
		print 'setUp...'
	def test_init(self):
	#定义测试初始化的函数
		d = Dict(a=1, b='test')
		#给d赋予Dict类，并赋值a、b
		self.assertEquals(d.a, 1)
		#判断d.a是否等于1
		self.assertEquals(d.b, 'test')
		#d.b是否等于’test‘
		self.assertTrue(isinstance(d, dict))
		#d是否属于dict的类
	def test_key(self):
	#定义测试key的函数
		d = Dict()
		#给d赋予Dict类
		d['key'] = 'value'
		#给key赋值value
		self.assertEquals(d.key, 'value')
		#判断赋值是否成功
	def test_attr(self):
		d = Dict()
		d['key'] = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], 'value')
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
	def tearDown(self):
		print 'tearDown...'