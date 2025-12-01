import re
import math
import functools
import sys

# file = open('test-input.txt')
file = open('input.txt')

file_blocks = []
free_space_sizes = []
is_file_block = True
for line in file:
  file_id = 0
  for char in line.strip():
    if is_file_block:
      file_blocks.extend([file_id] * int(char))
      file_id += 1
    else:
      free_space_sizes.append(int(char))
    is_file_block = not is_file_block

left_idx = 0
right_idx = len(file_blocks) - 1
curr_idx = 0
is_file_block = True
sum = 0
free_space = 0
free_space_idx = 0
while left_idx != right_idx:
  if is_file_block:
    sum += curr_idx * file_blocks[left_idx]
    if curr_idx < 20:
      print(file_blocks[left_idx], curr_idx)
    if file_blocks[left_idx] != file_blocks[left_idx+1]:
      is_file_block = False
    left_idx += 1
  else:
    if free_space == 0:
      free_space = free_space_sizes[free_space_idx]
      free_space_idx += 1
    sum += curr_idx * file_blocks[right_idx]
    if curr_idx < 20:
      print(file_blocks[right_idx], curr_idx)
    right_idx -= 1
    free_space -= 1
    if free_space == 0:
      is_file_block = True
  curr_idx += 1
  # if curr_idx % 1000 == 0:
  #   print(sum)
sum += curr_idx * file_blocks[left_idx]
if curr_idx < 20:
  print(file_blocks[left_idx], curr_idx)
print('final_index', curr_idx)
print(sum)