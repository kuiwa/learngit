'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''

def sum67(nums):
  sum = 0
  jump = False
  for n in nums:
    if n == 6:
      jump = True
    if jump:
      if n == 7:
        jump = False
      continue
    else:
      sum += n
  return sum