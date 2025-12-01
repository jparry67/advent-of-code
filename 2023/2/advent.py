import re

# file = open('test-input.txt')
file = open('input.txt')

# colorsAvailable = {
#   'red': 12,
#   'green': 13,
#   'blue': 14,
# }
total = 0

# for line in file:
#   line = line.rstrip()
#   game,cs = line.split(': ')
#   gameId = int(game.split(' ')[1])
#   colors = re.split('; |, ', cs)
#   addGameId = True
#   for color in colors:
#     n,c = color.split(' ')
#     if int(n) > colorsAvailable[c]:
#       addGameId = False
#   if addGameId:
#     total += gameId

for line in file:
  colorsAvailable = {
    'red': 0,
    'green': 0,
    'blue': 0,
  }
  line = line.rstrip()
  game,cs = line.split(': ')
  colors = re.split('; |, ', cs)
  for color in colors:
    n,c = color.split(' ')
    if int(n) > colorsAvailable[c]:
      colorsAvailable[c] = int(n)
  power = colorsAvailable['red'] * colorsAvailable['blue'] * colorsAvailable['green']
  total += power


print(total)