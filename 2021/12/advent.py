# file = open('test-input.txt')
file = open('input.txt')
# nums = [int(line) for line in file]
lines = [line.strip().split('-') for line in file]
edges = {}
for edge in lines:
  first,second = edge
  if first not in edges:
    edges[first] = set()
  if second not in edges:
    edges[second] = set()
  edges[first].add(second)
  edges[second].add(first)
# part 1
pathsToCheck = [{'lastCave':'start', 'smallCavesVisited': ['start']}]
successfulPaths = 0
while (len(pathsToCheck)):
  path = pathsToCheck.pop(0)
  for next in edges[path['lastCave']]:
    if not next in path['smallCavesVisited']:
      if next == 'end':
        successfulPaths += 1
      else:
        newPath = {'lastCave':next, 'smallCavesVisited':path['smallCavesVisited'].copy()}
        if next.islower():
          newPath['smallCavesVisited'].append(next)
        pathsToCheck.append(newPath)
print(successfulPaths)
# part 2
pathsToCheck = [{'path':['start'], 'smallCavesVisited': ['start'], 'smallCaveVisitedTwice':False}]
successfulPaths = 0
while (len(pathsToCheck)):
  path = pathsToCheck.pop(0)
  for next in edges[path['path'][-1]]:
    alreadyVisited = next in path['smallCavesVisited']
    if not alreadyVisited or (not path['smallCaveVisitedTwice'] and next != 'start'):
      if next == 'end':
        successfulPaths += 1
      else:
        newPath = {'path':path['path'] + [next], 'smallCavesVisited':path['smallCavesVisited'].copy(), 'smallCaveVisitedTwice':path['smallCaveVisitedTwice'] or alreadyVisited}
        if next.islower():
          newPath['smallCavesVisited'].append(next)
        pathsToCheck.append(newPath)
print(successfulPaths)
