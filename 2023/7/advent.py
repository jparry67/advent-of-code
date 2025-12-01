import re
import math
import functools

# file = open('test-input.txt')
file = open('input.txt')

total = 0
hands = []
possibleHands = {
  '5': 1, # Five of a kind
  '14': 2, # Four of a kind
  '23': 3, # Full house
  '113': 4, # Three of a kind
  '122': 5, # Two pair
  '1112': 6, # One pair
  '11111': 7, # High card
}
cards = {
  'A': 1,
  'K': 2,
  'Q': 3,
  'T': 5,
  '9': 6,
  '8': 7,
  '7': 8,
  '6': 9,
  '5': 10,
  '4': 11,
  '3': 12,
  '2': 13,
  'J': 14, #joker is weakest
}

for line in file:
  line.rstrip()
  hand,bid = line.split()
  hands.append([hand, int(bid)])

def GetHand(cards):
  cardDict = {}
  jCount = 0
  for card in cards:
    if (card == 'J'):
      jCount += 1
    else:
      cardDict[card] = cardDict[card]+1 if card in cardDict else 1
  sortedCounts = sorted([str(x) for x in cardDict.values()])
  if jCount == 5:
    sortedCounts = ['5']
  else:
    sortedCounts[-1] = str(int(sortedCounts[-1])+jCount)
  return possibleHands[''.join(sortedCounts)]

test_cases = [['23456',7],['23345',6],['22334',5],['23444',4],['22233',3],['23333',2],['22222',1]]
for case in test_cases:
  if GetHand(case[0]) != case[1]:
    print('ERROR:', case)

def CompareHands(x, y):
  xHand = GetHand(x[0])
  yHand = GetHand(y[0])
  if xHand < yHand:
    return 1
  if yHand < xHand:
    return -1
  for i in range(5):
    if cards[x[0][i]] < cards[y[0][i]]:
      return 1
    if cards[y[0][i]] < cards[x[0][i]]:
      return -1

# test_cases = [[['33333'],['22222'],-1],[['23456'],['34567'],1],[['33322'],['22233'],-1],[['28888'],['27777'],1]]
# for case in test_cases:
#   if CompareHands(case[0], case[1]) != case[2]:
#     print('ERROR:', case)

sortedHands = sorted(hands, key=functools.cmp_to_key(CompareHands))
for i,hand in enumerate(sortedHands):
  total += (i+1)*hand[1]
print(total)