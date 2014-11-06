# -*- coding: utf-8 -*-

words = open ("spell.words").readline()
words = map(lambda x: x.strip(), words)
print words