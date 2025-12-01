import re

# file = open('test-input.txt')
file = open('input.txt')

safe = 0

def check_safe(nums):
  is_safe = True
  increasing = nums[1] > nums[0]
  for i,_ in enumerate(nums):
    if i == 0:
      continue
    if (nums[i] == nums[i-1]) or (increasing and nums[i] < nums[i-1]) or (not increasing and nums[i] > nums[i-1]) or (abs(nums[i] - nums[i-1]) > 3):
      is_safe = False
      break
  return is_safe

for line in file:
  nums = list(map(int, line.split()))
  is_safe = check_safe(nums)
  if is_safe:
    print(nums, 'Safe without removing any level')
    safe += 1
  else:
    for i in range(len(nums)):
      nums_without_i = nums[:i] + nums[i+1:]
      is_safe = check_safe(nums_without_i)
      if is_safe:
        print(nums, 'Safe by removing level', i)
        safe += 1
        break
    if not is_safe:
      print(nums, 'Unsafe regardless of which level is removed')


print(safe)