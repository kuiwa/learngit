# -*- coding: utf-8 -*-

def big_diff(nums):
  min_n = nums[0]
  max_n = 0
  for n in nums:
    min_n = min(min_n, n)
    max_n = max(max_n, n)
  diff = max_n - min_n
  return diff
  
def min(v1, v2):
  if v1 <= v2: return v1
  else: return v2
  
def max(v1, v2):
  if v1 >= v2: return v1
  else: return v2


nums = [10, 2, 5, 6]
print big_diff(nums)