# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# file = open('test-input.txt')
file = open('input.txt')
# nums = [int(line) for line in file]
letters = []
priorities = 0
lines = []
for line in file:
  line = line.strip()
  lines.append(line)
  halfway = len(line) // 2
  first = line[:halfway]
  second = line[halfway:]
  common = set(first) & set(second)
  letter = common.pop()
  if (letter.islower()):
    priority = ord(letter)-96
    priorities += priority
  elif letter.isupper():
    priority = ord(letter)-38
    priorities += priority

priorities = 0
i = 0
while True:
  if i == len(lines):
    break
  common = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
  letter = common.pop()
  if (letter.islower()):
    priority = ord(letter)-96
    priorities += priority
  elif letter.isupper():
    priority = ord(letter)-38
    priorities += priority
  i += 3
print(priorities)