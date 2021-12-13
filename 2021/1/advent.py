# file = open('test-input.txt')
file = open('input.txt')
nums = [int(line) for line in file]
# part 1
prevNum = None
total = 0
for num in nums:
  if prevNum and num > prevNum:
    total += 1
  prevNum = num
print(total)
# part 2
total = 0
for i in range(3, len(nums)):
  if nums[i] > nums[i-3]:
    total += 1
print(total)