fname = "day 2/input.txt"
tot = 0

with open(fname) as f:
  lines = f.readlines()

  for l in lines:
    rpt = [int(n) for n in l.strip("\n").split(" ")]
    sign = None
    valid = 1
    for n_prev, n in zip(rpt[:-1], rpt[1:]):
      i = n - n_prev
      if abs(i) < 1 or abs(i) > 3:
        valid = 0
        break
        
      if sign != None and sign != i/abs(i):
        valid = 0
        break
      sign = i/abs(i)
    
    tot += valid

print(tot)
