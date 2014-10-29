# -*- coding: utf-8 -*-

import hashmap

# create a mapping of state to abbreviation
#states = hashmap.new()
#hashmap.set(states, 'New York', 'NY')
cities = hashmap.new()
hashmap.set(cities, 'NY', 'New York')

print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')

#print "OR State has: %s" % hashmap.get(states, 'OR')
# print every state abbreviation
#print '-' * 10
#hashmap.list(states)