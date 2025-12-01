import re
import math
import functools
import sys

sys.setrecursionlimit(1500)

# file = open('test-input.txt')
file = open('input.txt')

def is_valid_pos(pos, map):
  return pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0])

def get_map_val(pos, map):
  return map[pos[0]][pos[1]]

def continue_hike(path, map):
  curr = path[-1]
  curr_height = get_map_val(curr, map)
  if curr_height == 9:
    return [path]
  new_paths = []
  for possible_next in [(curr[0]-1,curr[1]),(curr[0]+1,curr[1]),(curr[0],curr[1]-1),(curr[0],curr[1]+1)]:
    if is_valid_pos(possible_next, map) and possible_next not in path:
      pn_height = get_map_val(possible_next, map)
      if pn_height - curr_height == 1:
        new_paths.extend(continue_hike(path + [possible_next], map))
  return new_paths

map = []
for line in file:
  map.append([int(char) for char in line.strip()])

paths = {}
for x,row in enumerate(map):
  for y,height in enumerate(row):
    if height == 0:
      paths[(x,y)] = continue_hike([(x,y)], map)

sum_peaks = 0
all_paths = 0
for start in paths:
  peaks = set()
  for path in paths[start]:
    peaks.add(path[-1])
  # print(start, len(peaks), peaks)
  sum_peaks += len(peaks)
  all_paths += len(paths[start])
print(sum_peaks)
print(all_paths)
