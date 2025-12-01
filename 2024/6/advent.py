import re
import math

def is_valid_pos(pos, map):
  return pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0])

def get_next_pos(pos, dir):
  if dir == 'up':
    return [pos[0]-1,pos[1]]
  elif dir == 'right':
    return [pos[0],pos[1]+1]
  elif dir == 'down':
    return [pos[0]+1,pos[1]]
  else:
    return [pos[0],pos[1]-1]
  
def get_map_val(pos, map):
  return map[pos[0]][pos[1]]

def would_create_loop(pos, dirs, dir_idx, map):
  visited = {pos[0]:{pos[1]:[dirs[dir_idx]]}}
  curr = pos
  while True:
    next_pos = get_next_pos(curr, dirs[dir_idx])
    if not is_valid_pos(next_pos, map):
      return False
    if get_map_val(next_pos, map) == '#':
      dir_idx = (dir_idx + 1) % 4
      next_pos = get_next_pos(curr, dirs[dir_idx])
    if next_pos == pos or next_pos[0] in visited and next_pos[1] in visited[next_pos[0]] and dirs[dir_idx] in visited[next_pos[0]][next_pos[1]]:
      return True
    if next_pos[0] in visited:
      if next_pos[1] in visited[next_pos[0]]:
        visited[next_pos[0]][next_pos[1]].append(dirs[dir_idx])
      else:
        visited[next_pos[0]][next_pos[1]] = [dirs[dir_idx]]
    else:
      visited[next_pos[0]] = {next_pos[1]: [dirs[dir_idx]]}
    curr = next_pos

# file = open('test-input.txt')
file = open('input.txt')

map = []
for line in file:
  map.append([char for char in line.strip()])

starting_position = []
for i,row in enumerate(map):
  if '^' in row:
    starting_position = [i,row.index('^')]

dirs = ['up','right','down','left']
dir_idx = 0
cur_pos = starting_position
count = 0
loop_count = 0
obstacles = set()
while is_valid_pos(cur_pos, map):
  if get_map_val(cur_pos, map) != 'X':
    count += 1
    map[cur_pos[0]][cur_pos[1]] = 'X'

  next_pos = get_next_pos(cur_pos, dirs[dir_idx])
  if not is_valid_pos(next_pos, map):
    break
  
  if get_map_val(next_pos, map) == '#':
    dir_idx = (dir_idx + 1) % 4
    next_pos = get_next_pos(cur_pos, dirs[dir_idx])
  elif (next_pos[0],next_pos[1]) not in obstacles and would_create_loop(cur_pos, dirs, (dir_idx + 1) % 4, map):
    # print(next_pos)
    # print(count, next_pos)
    obstacles.add((next_pos[0],next_pos[1]))
    loop_count += 1
  cur_pos = next_pos

print(count)
print(loop_count, len(obstacles), obstacles)
