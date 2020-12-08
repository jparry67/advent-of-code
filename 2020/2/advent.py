file = open("input.txt", "r")
input = [str(line).rstrip("\n") for line in file]
valid = 0
for line in input:
    nums,target,string = line.split(" ")
    min,max = map(int, nums.split("-"))
    char = target[0]
    # count = 0
    # for c in string:
    #     if c == char:
    #         count += 1
    # if count >= min and count <= max:
    #     valid += 1
    max -= 1
    min -= 1
    if max < len(string):
        if (string[min] == char or string[max] == char) and not (string[min] == char and string[max] == char):
            valid += 1
    elif min < len(string) and string[min] == char:
        valid += 1
print(valid)