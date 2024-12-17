def parse_input(fname):
  with open(fname) as f:
      lines = f.readlines()

  l1 = []
  l2 = []

  for l in lines:
    n1, n2 = l.strip("\n").split("   ")
    l1.append(int(n1))
    l2.append(int(n2))
  return l1, l2

l1, l2 = parse_input("./day 1/input.txt")
l1.sort()
l2.sort()

tot = 0
for n1, n2 in zip(l1, l2):
  tot += abs(n2 - n1)

print(f"Part 1 = {tot}")

# Part 2
counted = dict()
score = 0
for n1 in l1:
  if n1 not in counted:
    counted[n1] = l2.count(n1)
  score += n1*counted[n1]

print(f"Part 2 = {score}")