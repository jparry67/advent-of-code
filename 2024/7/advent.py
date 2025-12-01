import re
import math
import functools
import sys

sys.setrecursionlimit(1500)

# file = open('test-input.txt')
file = open('input.txt')

def can_hit_target(target, nums):
  if len(nums) == 0:
    return False
  if target < 0:
    return False    
  
  if len(nums) == 1 and nums[0] == target:
    return True
    
  if can_hit_target(target - nums[-1], nums[:-1]):
    return True
  if target % nums[-1] == 0 and can_hit_target(target // nums[-1], nums[:-1]):
    return True
  tarstr = str(target)
  numstr = str(nums[-1])
  if tarstr.endswith(numstr) and tarstr != numstr:
    if can_hit_target(int(tarstr[:-1*len(numstr)]), nums[:-1]):
      return True
    # else:
    #   print(target, nums[-1], int(tarstr[:-1*len(numstr)]), nums[:-1])
  
  return False

sum = 0
count = 0
for line in file:
  count += 1
  # if (count % 50):
  #   print(count)
  tarstr, numstr = line.strip().split(':')
  target = int(tarstr)
  nums = [int(num) for num in numstr.split()]
  
  if can_hit_target(target, nums):
    sum += target
print(sum)