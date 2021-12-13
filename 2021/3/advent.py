# file = open('test-input.txt')
file = open('input.txt')
# nums = [int(line) for line in file]
lines = [line.strip() for line in file]

def binToDec(bin):
  curr = 2 ** (len(bin)-1)
  dec = 0
  for num in bin:
    if num == '1':
      dec += curr
    curr //= 2
  return dec

# part 1
zeros = {}
ones = {}
for bin in lines:
  for i in range(len(bin)):
    if i not in zeros:
      zeros[i] = 0
      ones[i] = 0
    if bin[i] == '0':
      zeros[i] = zeros[i] + 1
    else:
      ones[i] = ones[i] + 1
gamma = ''
epsilon = ''
for i in range(len(zeros)):
  if zeros[i] > ones[i]:
    gamma = gamma + '0'
    epsilon = epsilon + '1'
  else:
    gamma = gamma + '1'
    epsilon = epsilon + '0'
print(binToDec(gamma) * binToDec(epsilon))
# part 2
o2 = lines
co2 = lines
index = 0
while (len(o2) > 1):
  ones = []
  zeros = []
  for val in o2:
    if val[index] == '1':
      ones.append(val)
    else:
      zeros.append(val)
  if len(zeros) > len(ones):
    o2 = zeros
  else:
    o2 = ones
  index += 1
index = 0
while (len(co2) > 1):
  ones = []
  zeros = []
  for val in co2:
    if val[index] == '1':
      ones.append(val)
    else:
      zeros.append(val)
  if len(zeros) > len(ones):
    co2 = ones
  else:
    co2 = zeros
  index += 1
print(binToDec(o2[0]) * binToDec(co2[0]))
