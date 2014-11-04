left1([1, 2, 3]) → [2, 3, 1]
left1([5, 11, 9]) → [11, 9, 5]
left1([7, 0, 0]) → [0, 0, 7]

def left1(nums):
  nums_r = []
  nums_swap = nums[0]
  for i in range(0, len(nums)-1):
    nums[i] = nums[i+1]
  nums[-1] = nums_swap
  return nums
