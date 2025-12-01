import re
import math
import functools
import sys

def is_valid_pos(pos, map):
  return pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0])

def get_map_val(pos, map):
  return map[pos[0]][pos[1]]

def get_possible_neighboring_map_positions(pos):
  return [(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1)]

def get_neighboring_map_positions(pos, map):
  possible_positions = get_possible_neighboring_map_positions(pos)
  return list(filter(lambda new_pos: is_valid_pos(new_pos, map), possible_positions))


# file = open('test-input.txt')
file = open('input.txt')

garden_map = []
available_plots = set()
for i,line in enumerate(file):
  for j,char in enumerate(line.strip()):
    available_plots.add((i,j))
  garden_map.append([char for char in line.strip()])

score = 0
groups = []

while available_plots:
  group = set()
  first_plot = next(iter(available_plots))
  plot_type = get_map_val(first_plot, garden_map)
  plots_to_check = [first_plot]
  area = 0
  perimeter = 0
  while plots_to_check:
    curr = plots_to_check.pop()
    available_plots.remove(curr)
    group.add(curr)
    area += 1
    for plot in get_possible_neighboring_map_positions(curr):
      if is_valid_pos(plot, garden_map) and get_map_val(plot, garden_map) == plot_type:
        if plot in available_plots and plot not in plots_to_check:
          plots_to_check.append(plot)
      else:
        perimeter += 1
  group_score = area * perimeter
  print(f"{plot_type}: {area} * {perimeter} = {group_score}")
  score += group_score
  groups.append(group)
print(score)

discounted_score = 0
for group in groups:
  corners = 0
  for plot in group:
    up = (plot[0]-1,plot[1])
    down = (plot[0]+1,plot[1])
    left = (plot[0],plot[1]-1)
    right = (plot[0],plot[1]+1)
    up_left = (plot[0]-1,plot[1]-1)
    down_left = (plot[0]+1,plot[1]-1)
    up_right = (plot[0]-1,plot[1]+1)
    down_right = (plot[0]+1,plot[1]+1)
    for corner_plots in [(up,left,up_left),(up,right,up_right),(down,left,down_left),(down,right,down_right)]:
      if corner_plots[0] not in group and corner_plots[1] not in group:
        # outer corner
        corners += 1
      elif corner_plots[0] in group and corner_plots[1] in group and corner_plots[2] not in group:
        # inner corner
        corners += 1
  score = corners * len(group)
  discounted_score += score
  print(f"{get_map_val(plot, garden_map)}: {len(group)} * {corners} = {score}")
print(discounted_score)