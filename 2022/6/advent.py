from aocd import submit

# file = open('test-input.txt')
file = open('input.txt')
answer = 0
for line in file:
    for i, char in enumerate(line):
        if len(set(line[i:i+14])) == 14:
            answer = i + 14
            break
        
print(answer)
# submit(answer, part="b", day=6, year=2022)