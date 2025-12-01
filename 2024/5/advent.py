import re

# file = open('test-input.txt')
file = open('input.txt')

reading_rules = True
rules = {}
sum = 0
invalid_nums = []
for line in file:
  if len(line) == 1:
    reading_rules = False
    continue

  if reading_rules:
    bef,aft = line.split('|')
    bef = int(bef)
    aft = int(aft)
    if bef in rules:
      rules[bef].add(aft)
    else:
      rules[bef] = set([aft])
  else:
    nums = list(map(int, line.split(',')))
    valid = True
    for i,num in enumerate(nums):
      for j in range(i+1, len(nums)):
        if nums[j] in rules and num in rules[nums[j]]:
          valid = False
    if valid:
      sum += nums[len(nums)//2]
    else:
      invalid_nums.append(nums)
print(sum)

new_sum = 0
for nums in invalid_nums:
  valid = False
  while not valid:
    valid = True
    for i,num in enumerate(nums):
      if not valid:
        break
      for j in range(i+1, len(nums)):
        if nums[j] in rules and num in rules[nums[j]]:
          valid = False
          num = nums.pop(j)
          nums.insert(i, num)
          break
  new_sum += nums[len(nums)//2]
print(new_sum)