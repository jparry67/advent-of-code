file = open("input.txt", "r")
input = [str(line) for line in file][0]
houses = {0: {0}}
for i in range(2):
    curr_x = 0
    curr_y = 0
    for j in range(i, len(input), 2):
        char = input[j]
        if char == '^':
            curr_y += 1
        elif char == '>':
            curr_x += 1
        elif char == '<':
            curr_x -= 1
        elif char == 'v':
            curr_y -= 1
        if curr_x not in houses:
            houses[curr_x] = {curr_y}
        else:
            houses[curr_x].add(curr_y)
num_houses = 0
for h in houses.values():
    num_houses += len(h)
print(num_houses)