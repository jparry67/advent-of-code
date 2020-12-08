file = open("input.txt", "r")
input = [str(line).rstrip(".\n") for line in file]

rules = {}
reversed_rules = {}
for line in input:
    outer,inner = line.split(" bags contain ")
    rules[outer] = {}
    innerBags = inner.split(", ")
    for bag in innerBags:
        if bag == "no other bags":
            break
        bag = bag.split(" bag")[0]
        amount = int(bag[0])
        bag = bag[2:]
        rules[outer][bag] = amount
        if bag in reversed_rules:
            reversed_rules[bag].append(outer)
        else:
            reversed_rules[bag] = [outer]

bagsToCheck = ["shiny gold"]
canContainShinyGold = set()
while len(bagsToCheck):
    if bagsToCheck[0] in reversed_rules:
        for bag in reversed_rules[bagsToCheck[0]]:
            if bag not in canContainShinyGold:
                canContainShinyGold.add(bag)
                bagsToCheck.append(bag)
    bagsToCheck.pop(0)
# print(canContainShinyGold)
# print(len(canContainShinyGold))

currentBags = {"shiny gold": 1}
nextBags = {}
totalBags = 0
while True:
    print(currentBags)
    updated = False
    for bag in list(currentBags):
        for innerBag in rules[bag].keys():
            updated = True
            if innerBag not in nextBags:
                nextBags[innerBag] = rules[bag][innerBag] * currentBags[bag]
            else:
                nextBags[innerBag] = nextBags[innerBag] + rules[bag][innerBag] * currentBags[bag]
        if not rules[bag]:
            if bag not in nextBags:
                nextBags[bag] = currentBags[bag]
            else:
                nextBags[bag] = nextBags[bag] + currentBags[bag]
        else:
            totalBags += currentBags[bag]
    currentBags = nextBags
    nextBags = {}
    if not updated:
        break
print(currentBags)
totalBags += sum(currentBags.values())
print(totalBags)
