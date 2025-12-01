import re
import math
import functools

# file = open('test-input.txt')
file = open('input.txt')

board = []
for line in file:
  board.append(line.strip())

xmas_count = 0
for i in range(len(board)):
  for j in range(len(board[i])):
    if board[i][j] == 'X':
      words = []
      # left
      if j >= 3:
        words.append(board[i][j] + board[i][j-1] + board[i][j-2] + board[i][j-3])
      # right
      if j < len(board[i])-3:
        words.append(board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3])
      # up
      if i >= 3:
        words.append(board[i][j] + board[i-1][j] + board[i-2][j] + board[i-3][j])
      # down
      if i < len(board)-3:
        words.append(board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])
      # up left
      if j >= 3 and i >= 3:
        words.append(board[i][j] + board[i-1][j-1] + board[i-2][j-2] + board[i-3][j-3])
      # up right
      if j < len(board[i])-3 and i >= 3:
        words.append(board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3])
      # down left
      if j >= 3 and i < len(board)-3:
        words.append(board[i][j] + board[i+1][j-1] + board[i+2][j-2] + board[i+3][j-3])
      # down right
      if j < len(board[i])-3 and i < len(board)-3:
        words.append(board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3])
      for word in words:
        if word == 'XMAS':
          xmas_count += 1
print(xmas_count)

x_mas_count = 0
for i in range(len(board)):
  for j in range(len(board[i])):
    if board[i][j] == 'A' and i >= 1 and j >= 1 and i < len(board)-1 and j < len(board[i])-1 and set([board[i-1][j-1],board[i+1][j+1]]) == set(['M','S']) and set([board[i-1][j+1],board[i+1][j-1]]) == set(['M','S']):
      x_mas_count += 1
print(x_mas_count)