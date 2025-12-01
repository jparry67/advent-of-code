import re
import math

# file = open('test-input.txt')
file = open('input.txt')

total = 1
#part 1
# races = [list(map(int, line.split()[1:])) for line in file]
#part 2
races = [[int(''.join(line.split()[1:]))] for line in file]
print(races)
for i in range(len(races[0])):
  time = races[0][i]
  distance = races[1][i]
  a = -1
  b = time
  c = distance*-1
  quad = math.sqrt(b**2-4*a*c)
  left = math.ceil((b*-1+quad)/2/a+.001)
  right = math.floor((b*-1-quad)/2/a-.001)
  total *= right-left+1
print(total)