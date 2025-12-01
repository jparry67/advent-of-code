import re
import math
import functools
import sys

file = open('test-input.txt')
# file = open('input.txt')

def get_fifteen_blinks(stones):
  for _ in range(15):
    new_stones = []
    for stone in stones:
      if stone == 0:
        new_stones.append(1)
      elif len(str(stone)) % 2 == 0:
        midpoint = len(str(stone)) // 2
        new_stones.extend([int(str(stone)[:midpoint]), int(str(stone)[midpoint:])])
      else:
        new_stones.append(stone * 2024)
    stones = new_stones
  return stones

stones = []
for line in file:
  stones = [int(num) for num in line.split()]

fifteen_level_memo = {}
for i in range(75//15):
  print(i*15, len(stones), len(fifteen_level_memo))
  new_stones = []
  for stone in stones:
    if stone not in fifteen_level_memo:
      fifteen_level_memo[stone] = get_fifteen_blinks([stone])
    new_stones.extend(fifteen_level_memo[stone])
  stones = new_stones