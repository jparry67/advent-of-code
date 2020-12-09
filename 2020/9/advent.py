def checkSum(target, nums):
    possible = set()
    for n in nums:
        if n in possible:
            return True
        possible.add(target-n)

file = open("input.txt", "r")
input = [int(line) for line in file]

preamble = set()
sums = set()
invalid = -1
for i,n in enumerate(input[25:]):
    i += 25
    if not checkSum(n, input[i-25:i]):
        invalid = n # solution for part 1
        break

index1 = 0
index2 = 1
sum = input[0] + input[1]
range = []
while True:
    if sum == invalid:
        range = input[index1:index2+1]
        break
    if sum < invalid or index2-index1 == 1:
        index2 += 1
        sum += input[index2]
    else:
        sum -= input[index1]
        index1 += 1

print(min(range) + max(range))