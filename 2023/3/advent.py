import re

# file = open('test-input.txt')
file = open('input.txt')

def checkSymbol(char):
  # if str.isdigit(char) or char == '.':
  #   return False
  # return True
  return char == '*'

def isAdjacent(table, row, column):
  # top left
  if row > 0 and column > 0 and checkSymbol(table[row-1][column-1]):
      return (row-1,column-1)
  # top
  if row > 0 and checkSymbol(table[row-1][column]):
      return (row-1,column)
  # top right
  if row > 0 and column < len(table[0])-1 and checkSymbol(table[row-1][column+1]):
      return (row-1,column+1)
  # right
  if column < len(table[0])-1 and checkSymbol(table[row][column+1]):
      return (row,column+1)
  # bottom right
  if row < len(table)-1 and column < len(table[0])-1 and checkSymbol(table[row+1][column+1]):
      return (row+1,column+1)
  # bottom
  if row < len(table)-1 and checkSymbol(table[row+1][column]):
      return (row+1,column)
  # bottom left
  if row < len(table)-1 and column > 0 and checkSymbol(table[row+1][column-1]):
      return (row+1,column-1)
  # left
  if column > 0 and checkSymbol(table[row][column-1]):
      return (row,column-1)
  # if none return
  return None
table = []
total1 = 0
total2 = 0

for line in file:
  line = line.rstrip()
  # table.append([char for char in line])
  table.append(line)

# for j,row in enumerate(table):
#   numStartingIndex = None
#   includeNumber = False
#   for i,char in enumerate(row):
#     if str.isdigit(char):
#       if numStartingIndex == None:
#         numStartingIndex = i
#       includeNumber = includeNumber or isAdjacent(table, j, i)
#       if i == len(row)-1 and includeNumber:
#         num = int(row[numStartingIndex:])
#         total1 += num
#     else:
#       if numStartingIndex != None:
#         num = int(row[numStartingIndex:i])
#         numStartingIndex = None
#         if includeNumber:
#           total1 += num
#           includeNumber = False

gearLocations = {}

for j,row in enumerate(table):
  numStartingIndex = None
  gear = None
  for i,char in enumerate(row):
    if str.isdigit(char):
      if numStartingIndex == None:
        numStartingIndex = i
      nextGear = isAdjacent(table, j, i)
      if gear is not None and nextGear is not None and gear != nextGear:
         print('uh oh')
      if nextGear is not None:
         gear = nextGear
      if i == len(row)-1 and gear is not None:
        num = int(row[numStartingIndex:])
        if gear in gearLocations:
           gearLocations[gear].append(num)
        else:
           gearLocations[gear] = [num]
    else:
      if numStartingIndex != None:
        num = int(row[numStartingIndex:i])
        numStartingIndex = None
        if gear is not None:
          if gear in gearLocations:
            gearLocations[gear].append(num)
          else:
            gearLocations[gear] = [num]
          gear = None
for key in gearLocations.keys():
  if len(gearLocations[key]) == 2:
     total2 += gearLocations[key][0] * gearLocations[key][1]

print(total2)