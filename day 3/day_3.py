import regex as re

s = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('day 3/input.txt') as f:
  s = f.read()



pat = 'mul\(\d{1,3},\d{1,3}\)'
# pat = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

m = re.findall(pat, s)

tot = 0
enable = True
for exp in m:
  n1, n2 = exp[4:-1].split(',')
  n = int(n1)*int(n2)
  tot += n
  # print(exp)
print("Part 1 = ", tot)


pat = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
m = re.findall(pat, s)


tot = 0
enable = True
for exp in m:
  if exp == 'do()':
    enable = True
  elif exp == "don't()":
    enable = False
  elif enable:
    n1, n2 = exp[4:-1].split(',')
    n = int(n1)*int(n2)
    tot += n
  # print(exp)

print("Part 2 = ", tot)