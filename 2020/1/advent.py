file = open("input.txt")
nums = [int(line) for line in file]
seenNums = set()
sums = {}
for n in nums:
    # Part 1
    # if 2020 - n in seenNums:
    #     print(n * (2020-n))
    #     break
    # seenNums.add(n)

    # Part 2
    if 2020 - n in sums:
        print(n*sums[2020-n][0]*sums[2020-n][1])
    for num in seenNums:
        sums[num+n] = [num,n]
    seenNums.add(n)