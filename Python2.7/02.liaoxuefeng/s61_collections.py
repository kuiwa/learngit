#!/usr/bin/env python
# -*- coding: utf-8 -*-

#nametuple('名称', [属性list])
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print c.x
print c.y
print c.r

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q
q.popleft()
print q

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']