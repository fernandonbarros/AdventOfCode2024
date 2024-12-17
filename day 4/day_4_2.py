def is_x_mas(grid, row, col):
  if (row < 1 or row >= len(grid)-1) or (col < 1 or col >= len(grid[0])-1):
    return 0

  fwd = grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]
  bwd = grid[row+1][col-1] + grid[row][col] + grid[row-1][col+1]

  if (fwd == 'MAS' or fwd == 'SAM') and (bwd == 'MAS' or bwd == 'SAM'):
    return 1
  
  return 0

with open('day 4/input.txt') as f:
  lines = f.readlines()


lines = [l.strip('\n') for l in lines]

tot = 0
for row in range(len(lines)):
  for col in range(len(lines[row])):
    tot += is_x_mas(lines, row, col)

print(tot)