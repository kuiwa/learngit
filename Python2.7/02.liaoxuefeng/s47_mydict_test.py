#!/usr/bin/env python
# -*- coding: utf-8 -*-

#��Ԫ����

import unittest

from s47_mydict import Dict

class TestDict(unittest.TestCase):
#������Ե�Ԫ����
	def setUp(self):
		print 'setUp...'
	def test_init(self):
	#������Գ�ʼ���ĺ���
		d = Dict(a=1, b='test')
		#��d����Dict�࣬����ֵa��b
		self.assertEquals(d.a, 1)
		#�ж�d.a�Ƿ����1
		self.assertEquals(d.b, 'test')
		#d.b�Ƿ���ڡ�test��
		self.assertTrue(isinstance(d, dict))
		#d�Ƿ�����dict����
	def test_key(self):
	#�������key�ĺ���
		d = Dict()
		#��d����Dict��
		d['key'] = 'value'
		#��key��ֵvalue
		self.assertEquals(d.key, 'value')
		#�жϸ�ֵ�Ƿ�ɹ�
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