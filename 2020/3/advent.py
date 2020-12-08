file = open("input.txt", "r")
input = [str(line).rstrip("\n") for line in file]

arr = []
for s in range(1,8,2):
    print(s)
    i = 0
    count = 0
    for line in input:
        if line[i % len(line)] == '#':
            count += 1
        i += s
    arr.append(count)
s = 1
count = 0
i = 0
for l in range(0,len(input),2):
    if input[l][i % len(input[l])] == '#':
        count += 1
    i += s
arr.append(count)
print(arr)
product = 1
for a in arr:
    product *= a
print(product)