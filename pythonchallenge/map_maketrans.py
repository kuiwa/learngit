# -*- coding: utf-8 -*-

import string
map = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
s = open('map.txt')
print s.read().translate(map)
w = 'map'
print w.translate(map)