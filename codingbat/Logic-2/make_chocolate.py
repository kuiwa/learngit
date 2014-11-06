# -*- coding: utf-8 -*-
'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''
def make_chocolate(small, big, goal):
  small_kilo = 1
  big_kilo = 5
  i = 1
  j = 0
  for i in xrange(big+1):
    for j in xrange(small+1):
      sum = i * 5 + j 
      if sum == goal: return j
  return -1
  
print make_chocolate(4, 1, 9)

# here is the way without any loop which can be passed on the codingbat.com
def make_chocolate(small, big, goal):
  sum = 0
  mod = goal % 5
  div = goal / 5
  if big >= div and mod == 0: return 0
  elif small >= mod and div == 0: return mod
  elif big >= div and small >= mod: return mod
  elif big < div and small >= goal - big * 5: return goal - big * 5
  else: return -1