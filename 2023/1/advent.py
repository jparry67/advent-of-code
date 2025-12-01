# file = open('test-input.txt')
file = open('input.txt')

total = 0
strings = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

for line in file:
  first = None
  firstI = None
  last = None
  lastI = None
  for i, char in enumerate(line):
    if str.isdigit(char):
      if first is None:
        first = char
        firstI = i
      last = char
      lastI = i
  for sol in strings:
    lpos = line.find(sol)
    if lpos != -1:
      if firstI is None or lpos < firstI:
        first = strings[sol]
        firstI = lpos
    rpos = line.rfind(sol)
    if rpos != -1:
      if lastI is None or rpos > lastI:
        last = strings[sol]
        lastI = rpos
  n = int(first + last)
  print(line, n)
  total += n


print(total)