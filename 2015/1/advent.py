
file = open("input.txt", "r")
input = [str(line) for line in file][0]
floor = 0
index = 0
for char in input:
    index += 1
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
        if floor < 0:
            print(index)
            break

# print(floor)