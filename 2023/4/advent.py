import re
import math
import functools

# file = open('test-input.txt')
file = open('input.txt')

total1 = 0
total2 = 0
copiesLeft = []
for line in file:
  line.rstrip()
  _,nums = line.split(':')
  winning,have = [set(ns.split()) for ns in nums.split('|')]
  numMatches = len(have.intersection(winning))
  total1 += math.floor(pow(2, numMatches-1))
  total2 += 1 + len(copiesLeft)
  newCopiesLeft = []
  if (numMatches):
    for _ in range(len(copiesLeft)+1):
      newCopiesLeft.append(numMatches)
  for c in copiesLeft:
    if c > 1:
      newCopiesLeft.append(c-1)
  copiesLeft = newCopiesLeft
print(total2)