# file = open('test-input.txt')
file = open('input.txt')
# nums = [int(line) for line in file]
lines = [line for line in file]
# part 1
horizontal = 0
depth = 0
for command in lines:
  direction,amount = command.split(' ')
  amount = int(amount)
  if direction == 'forward':
    horizontal += amount
  elif direction == 'down':
    depth += amount
  elif direction == 'up':
    depth -= amount
print(horizontal * depth)
# part 2
horizontal = 0
depth = 0
aim = 0
for command in lines:
  direction,amount = command.split(' ')
  amount = int(amount)
  if direction == 'forward':
    horizontal += amount
    depth += aim * amount
  elif direction == 'down':
    aim += amount
  elif direction == 'up':
    aim -= amount
print(horizontal * depth)