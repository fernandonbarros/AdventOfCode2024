import numpy as np

def check_array(a):
  d = np.diff(a)
  signs = np.sign(d)
  safe = (signs == 1).all() or (signs == -1).all()
  safe = safe and np.logical_and(abs(d) >= 1, abs(d) <= 3).all()

  return safe

fname = "day 2/input.txt"
tot = 0

with open(fname) as f:
  lines = f.readlines()

  for l in lines:
    rpt = np.array([int(n) for n in l.strip("\n").split(" ")])

    if check_array(rpt):
      tot += 1
      print(rpt, '- safe')
      continue
    else:
      for i in range(len(rpt)):
        rpt_safe = np.delete(rpt, i)
        # print(rpt_safe)
        if check_array(rpt_safe):
          tot += 1
          print(rpt_safe, '- safe')
          break
    # print(rpt, '- not safe')
    

print(tot)
