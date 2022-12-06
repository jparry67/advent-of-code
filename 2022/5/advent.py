
from aocd import submit

# file = open('test-input.txt')
file = open('input.txt')
answer = 0
stacks = []
num_stacks = 9
for i in range(num_stacks):
    stacks.append([])
for line in file:
    if line[1] == '1':
        break
    for i in range(num_stacks):
        crate = line[4*i:4*i+3].strip()
        if crate:
            stacks[i].insert(0, crate.strip('[]'))

for line in file:
    if not line.strip():
        continue
    num,line = line.strip().strip('move ').split(' from ')
    from_stack,to_stack = line.split(' to ')
    stacks[int(to_stack)-1].extend(stacks[int(from_stack)-1][-int(num):])
    stacks[int(from_stack)-1] = stacks[int(from_stack)-1][:-int(num)]
    # for _ in range(int(num)):
    #     stacks[int(to_stack)-1].append(stacks[int(from_stack)-1].pop())

print(stacks)
answer = ''.join(map(lambda stack: stack[-1], stacks))
print(answer)
submit(answer, part="b", day=5, year=2022)