'''
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''

def sum13(nums):
  if not len(nums):
    return 0
  sum = 0
  i = 0
  continue_no = False
  continue_next = False
  for i in nums:

    if i == 13:
      continue_no = True
      continue_next = True
    else:
      pass
    if continue_no:
      continue_no = False
      continue
    elif continue_next:
      continue_next = False     
      continue
    else: 
      sum += i
  return sum
