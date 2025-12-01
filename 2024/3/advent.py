import re

# file = open('test-input.txt')
file = open('input.txt')

command = ''
for line in file:
  command = command + line.strip()

sum = 0
valid = re.sub("don't\(\).*?do\(\)", '', command)
matches = re.findall('mul\((\d+)\,(\d+)\)', valid)
for match in matches:
  sum += int(match[0])*int(match[1])

print(sum)