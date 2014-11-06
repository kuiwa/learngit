#!/usr/bin/env python
# -*- coding: utf-8 -*-

#µ¥Ôª²âÊÔ
#mydict.py
class Dict(dict):
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribut '%s'" % key)
			
	def __setattr__(self, key, value):
		self[key] = value