# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data
from aocd import submit

# file = open('test-input.txt')
file = open('input.txt')
answer = 0
for line in file:
    first,second = line.strip().split(',')
    f = list(map(int, first.split('-')))
    s = list(map(int, second.split('-')))
    # part 1
    # if f[0] <= s[0] and f[1] >= s[1]:
    #     answer += 1
    # elif f[0] >= s[0] and  f[1] <= s[1]:
    #     answer += 1

    # part 2
    if s[0] >= f[0] and s[0] <= f[1] or s[1] >= f[0] and s[1] <= f[1]:
        answer += 1
    elif f[0] >= s[0] and f[0] <= s[1] or f[1] >= s[0] and f[1] <= s[1]:
        print(first, second)
        answer += 1

print(answer)
# submit(answer, part="b", day=4, year=2022)