import re
import math
import functools

# file = open('test-input.txt')
file = open('input.txt')

numSteps = 0
steps = None
nodes = {}
for line in file:
  line = line.rstrip()
  if steps is None:
    steps = line
    continue
  if line == '':
    continue
  node,roads = line.split(' = ')
  roads = roads.strip('()')
  nodes[node] = roads.split(', ')

# part 1
# currNode = 'AAA'
# currStepIndex = 0
# while currNode != 'ZZZ':
#   currNode = nodes[currNode][0 if steps[currStepIndex] == 'L' else 1]
#   numSteps += 1
#   currStepIndex = (currStepIndex + 1) % len(steps)
# print(numSteps)

# part 2
currNodes = []
zIndices = []
for node in list(nodes.keys()):
  if node[2] == 'A':
    currNodes.append(node)
    zIndices.append([])
print(currNodes)

intervals = []
for i,node in enumerate(currNodes):
  print(node)
  stepCounts = []
  currStepIndex = 0
  currNode = node
  done = False
  while not done:
    currNode = nodes[currNode][0 if steps[currStepIndex] == 'L' else 1]
    numSteps += 1
    currStepIndex = (currStepIndex + 1) % len(steps)
    if currNode[2] == 'Z':
      stepCounts.append(numSteps)
      if len(stepCounts) >= 3 and stepCounts[-1]-stepCounts[-2] == stepCounts[-2]-stepCounts[-3]:
        intervals.append(stepCounts[-1]-stepCounts[-2])
        done = True

currMulltiple = intervals[0]
for interval in intervals:
  numStepsV3 = currMulltiple
  while (numStepsV3 % interval != 0) or (numStepsV3 % currMulltiple != 0):
    numStepsV3 += currMulltiple
  currMulltiple = numStepsV3
  print(currMulltiple)
print('yay')
