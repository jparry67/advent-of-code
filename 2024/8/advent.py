import re
import math
import functools
import sys

sys.setrecursionlimit(1500)

# file = open('test-input.txt')
file = open('input.txt')

max_i = 0
max_j = 0
frequencies = {}
for i,line in enumerate(file):
  max_i = i
  for j,char in enumerate(line.strip()):
    max_j = j
    if char != '.':
      if char not in frequencies:
        frequencies[char] = {'antennas': [], 'antinodes': []}
      for prev_antenna in frequencies[char]['antennas']:
        anti_i = i - (prev_antenna[0] - i)
        anti_j = j - (prev_antenna[1] - j)
        frequencies[char]['antinodes'].append((anti_i,anti_j))
        anti_i = prev_antenna[0] - (i - prev_antenna[0])
        anti_j = prev_antenna[1] - (j - prev_antenna[1])
        frequencies[char]['antinodes'].append((anti_i,anti_j))
      frequencies[char]['antennas'].append((i,j))

all_antinodes = set()
for frequency in frequencies:
  for antinode in frequencies[frequency]['antinodes']:
    if antinode[0] >= 0 and antinode[0] <= max_i and antinode[1] >= 0 and antinode[1] <= max_j:
      all_antinodes.add(antinode)
print(len(all_antinodes))

# part 2
all_antinodes_2 = set()
for frequency in frequencies:
  for i,antenna_1 in enumerate(frequencies[frequency]['antennas']):
    all_antinodes_2.add(antenna_1)
    for j,antenna_2 in enumerate(frequencies[frequency]['antennas'][i+1:]):
      diff_x = antenna_1[0] - antenna_2[0]
      diff_y = antenna_1[1] - antenna_2[1]
      curr_x = antenna_2[0] - diff_x
      curr_y = antenna_2[1] - diff_y
      while curr_x >= 0 and curr_x <= max_i and curr_y >= 0 and curr_y <= max_j:
        all_antinodes_2.add((curr_x,curr_y))
        curr_x -= diff_x
        curr_y -= diff_y
      diff_x = antenna_2[0] - antenna_1[0]
      diff_y = antenna_2[1] - antenna_1[1]
      curr_x = antenna_1[0] - diff_x
      curr_y = antenna_1[1] - diff_y
      while curr_x >= 0 and curr_x <= max_i and curr_y >= 0 and curr_y <= max_j:
        all_antinodes_2.add((curr_x,curr_y))
        curr_x -= diff_x
        curr_y -= diff_y
print(len(all_antinodes_2))