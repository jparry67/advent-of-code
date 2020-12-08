file = open("input.txt", "r")
input = [str(line).rstrip("\n") for line in file]
input.append("")

count = 0
currGroup = set()
firstLine = True
for line in input:
    if line == "":
        count += len(currGroup)
        currGroup = set()
        firstLine = True
    else:
        newSet = set()
        for letter in line:
            newSet.add(letter)
        if firstLine:
            currGroup = newSet
            firstLine = False
        else:
            currGroup = currGroup.intersection(newSet)
print(count)