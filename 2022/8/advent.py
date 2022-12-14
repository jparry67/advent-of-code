from utils import Fns

class Solution():

  def run(self, input):
    answer = 0
    grid = []
    visible_grid = []
    for line in input.split('\n'):
      grid.append([[int(num),False] for num in line])
    
    for i in range(len(grid)):
      tallest = -1
      for j in range(len(grid[i])):
        if grid[i][j][0] > tallest:
          tallest = grid[i][j][0]
          grid[i][j][1] = True
      tallest = -1
      for j in range(len(grid[i])-1, -1, -1):
        if grid[i][j][0] > tallest:
          tallest = grid[i][j][0]
          grid[i][j][1] = True
      
    for j in range(len(grid[0])):
      tallest = -1
      for i in range(len(grid)):
        if grid[i][j][0] > tallest:
          tallest = grid[i][j][0]
          grid[i][j][1] = True
      tallest = -1
      for i in range(len(grid)-1, -1, -1):
        if grid[i][j][0] > tallest:
          tallest = grid[i][j][0]
          grid[i][j][1] = True

  
    # for row in grid:
    #   print(row)
    #   for tree in row:
    #     if tree[1]:
    #       answer += 1


    for i in range(len(grid)):
      for j in range(len(grid[i])):
        h = grid[i][j][0]
        left_count = 0
        left_j = j-1
        while (left_j >= 0):
          left_count += 1
          if grid[i][left_j][0] >= h:
            break
          left_j -= 1
        right_count = 0
        right_j = j+1
        while (right_j < len(grid[i])):
          right_count += 1
          if grid[i][right_j][0] >= h:
            break
          right_j += 1
        up_count = 0
        up_i = i-1
        while (up_i >= 0):
          up_count += 1
          if grid[up_i][j][0] >= h:
            break
          up_i -= 1
        down_count = 0
        down_i = i+1
        while (down_i < len(grid[i])):
          down_count += 1
          if grid[down_i][j][0] >= h:
            break
          down_i += 1
        print(left_count,right_count,up_count,down_count)
        score = left_count * right_count * up_count * down_count
        if score > answer:
          answer = score
    return answer