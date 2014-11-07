# -*- coding: utf-8 -*-
'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small, big, goal):
  small_inch = 1
  big_inch = 5
  for i in xrange(small+1):
    for j in xrange(big+1):
      plus_goal = small_inch * i + big_inch * j
      if plus_goal == goal:
        return True
  return False
print make_bricks(3, 2, 10)

# here is another way without any loops that can be passed on the codingbat.com
def make_bricks(small, big, goal):
  sum = 0
  mod = goal % 5
  div = goal / 5
  if big >= div and mod == 0: return True
  elif small >= mod and div == 0: return True
  elif big >= div and small >= mod: return True
  elif big < div and small >= goal - big * 5: return True
  else: return False