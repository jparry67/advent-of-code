file = open("input.txt", "r")
input = [str(line).rstrip("\n") for line in file]
wrappingPaper = 0
ribbon = 0
for line in input:
    l,w,h = [int(x) for x in line.split("x")]
    wrappingPaper += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
    ribbon += (l+w+h)*2 - max(l,w,h)*2 + l*w*h
print(wrappingPaper)
print(ribbon)