file = open("input.txt", "r")
input = [str(line).rstrip(".\n") for line in file]

nopIndices = []
jmpIndices = []
for i,line in enumerate(input):
    if line.split()[0] == "nop":
        nopIndices.append(i)
    if line.split()[0] == "jmp":
        jmpIndices.append(i)
print(nopIndices)

for changeIndex in jmpIndices:
    runInstructions = set()
    accumulator = 0
    index = 0
    success = False
    while True:
        if index in runInstructions:
            print("index",changeIndex,"failed")
            break
        if index == len(input):
            print("index",changeIndex,"success")
            success = True
            break
        runInstructions.add(index)
        comm,val = input[index].split()
        if comm == "nop" or changeIndex == index:
            index += 1
        elif comm == "acc":
            index += 1
            accumulator += int(val)
        elif comm == "jmp":
            index += int(val)
    if success:
        print(accumulator)
        break