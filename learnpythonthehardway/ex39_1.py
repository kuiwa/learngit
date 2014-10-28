# -*- coding: utf-8 -*-

things = ['a', 'b', 'c', 'd']

print things[1]

things[1] = 'z'
print things[1]
print things

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}

print stuff
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff
print stuff[1]
print stuff[2]

del stuff['city']
del stuff[1]
del stuff[2]
print stuff