# file = open('test-input.txt')
file = open('input.txt')

you_dict = {'X':3,'Y':6,'Z':9}
opp_dict = {'A':0,'B':3,'C':6}
you_list = ['X','Y','Z']
opp_index = {'A':0,'B':1,'C':2}

score = 0
new_score = 0
for line in file:
  opp, you = line.split()
  if you == 'X':
    you = you_list[(opp_index[opp]-1) % 3]
  elif you == 'Y':
    you = you_list[(opp_index[opp]) % 3]
  elif you == 'Z':
    you = you_list[(opp_index[opp]+1) % 3]
  if you == 'X':
    score += 1
  if you == 'Y':
    score += 2
  if you == 'Z':
    score += 3
  game_score = you_dict[you] - opp_dict[opp]
  if game_score < 0:
    game_score += 9
  if game_score == 9:
    game_score -= 9
  # print(game_score)
  score += game_score


print(score)




















# nums = [int(line) for line in file]

# calories = 0
# mostCalories = 0
# top3 = [0, 0, 0]
# for line in file:
#   if line != '\n':
#     calories += int(line)
#   else:
#     # part 1
#     if calories > mostCalories:
#       mostCalories = calories
#     # part 2
#     x = min(top3)
#     if calories > x:
#       top3.remove(x)
#       top3.append(calories)

#     calories = 0
# print(mostCalories)
# print(top3)
# print(sum(top3))
  
