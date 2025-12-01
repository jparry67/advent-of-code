# file = open('test-input.txt')
file = open('input.txt')

left = []
right = []

for line in file:
  l,r = line.split()
  left.append(int(l))
  right.append(int(r))
print(left,right)
left.sort()
right.sort()
print(left,right)
total = 0
for i in range(len(left)):
  total += abs(left[i]-right[i])
print(total)

right_counts = {}
for r in right:
  if r in right_counts:
    right_counts[r] += 1
  else:
    right_counts[r] = 1
print(right_counts)
similarity_score = 0
for l in left:
  if l in right_counts:
    similarity_score += l * right_counts[l]
print(similarity_score)