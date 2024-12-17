def find_word(grid, word, row, col, dir):
  DIRS = {
    'N': (-1, 0),
    'NE': (-1, 1),
    'E': (0, 1),
    'SE': (1, 1),
    'S': (1, 0),
    'SW': (1, -1),
    'W': (0, -1),
    'NW': (-1, -1)
    }
  
  if word == '':
    return []
  if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])):
    return None
  if word[0] != grid[row][col]:
    return None
  i = row + DIRS[dir][0]
  j = col + DIRS[dir][1]

  # if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
  #   return None
  
  pos = find_word(grid, word[1:], i, j, dir)

  return None if pos == None else [(row, col)] + pos

with open('day 4/input.txt') as f:
  lines = f.readlines()


lines = [l.strip('\n') for l in lines]

words = []
for row in range(len(lines)):
  for col in range(len(lines[row])):
    for d in ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'):
      pos = find_word(lines, 'XMAS', row, col, dir=d)
      if not pos == None:
        words.append(pos)

print(len(words))