from utils import Fns

class Solution():

  def check_next(self, head_pos, tail_pos):
    # diagonal up right
    if head_pos[0] - tail_pos[0] > 1 and head_pos[1] - tail_pos[1] > 1:
      return (head_pos[0]-1,head_pos[1]-1)
    # diagonoal up left
    if tail_pos[0] - head_pos[0] > 1 and head_pos[1] - tail_pos[1] > 1:
      return (head_pos[0]+1,head_pos[1]-1)
    # diagonal down right
    if head_pos[0] - tail_pos[0] > 1 and tail_pos[1] - head_pos[1] > 1:
      return (head_pos[0]-1,head_pos[1]+1)
    # diagonoal down left
    if tail_pos[0] - head_pos[0] > 1 and tail_pos[1] - head_pos[1] > 1:
      return (head_pos[0]+1,head_pos[1]+1)

    # right
    if head_pos[0] - tail_pos[0] > 1:
      return (head_pos[0]-1,head_pos[1])
    # left
    if tail_pos[0] - head_pos[0] > 1:
      return (head_pos[0]+1,head_pos[1])
    # up
    if head_pos[1] - tail_pos[1] > 1:
      return (head_pos[0],head_pos[1]-1)
    # down
    if tail_pos[1] - head_pos[1] > 1:
      return (head_pos[0],head_pos[1]+1)
    return tail_pos

  def move(self, curr_positions, direction):
    if direction == 'R':
      curr_positions[0][0] = curr_positions[0][0] + 1
    if direction == 'L':
      curr_positions[0][0] = curr_positions[0][0] - 1
    if direction == 'U':
      curr_positions[0][1] = curr_positions[0][1] + 1
    if direction == 'D':
      curr_positions[0][1] = curr_positions[0][1] - 1
    
    for i in range(1, len(curr_positions)):
      curr_positions[i] = self.check_next(curr_positions[i-1], curr_positions[i])


  def run(self, input):
    touched_positions = set()
    curr_positions = [[0,0],(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    for i,line in enumerate(input.split('\n')):
      direction,amount = line.strip().split()
      for _ in range(int(amount)):
        self.move(curr_positions, direction)
        touched_positions.add(curr_positions[-1])
        # print(curr_positions[-1])
    
    result = []
    for i in range(-85,195):
      result.append([])
      for j in range(-270,50):
        if i == 0 and j == 0:
          result[i+85].append('s')
        if (j,i) in touched_positions:
          result[i+85].append('#')
        else:
          result[i+85].append('.')
    for i in range(len(result)-1,-1,-1):
      print(''.join(result[i]))
    answer = len(touched_positions)
    return answer