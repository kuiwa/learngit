# -*- coding: utf-8 -*-

'''Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

def array123(nums):
  num123 = [1, 2, 3]
  for i in range(len(nums)):
    if nums[i:i+3] == num123:
      return True
  return False
