'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''
def rotate_left3(nums):
  num_sum = []
  for i in range(1,len(nums)):
    num_sum.append(nums[i])
  num_sum.append(nums[0])
  return num_sum
