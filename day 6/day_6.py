turn = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

step = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

with open('day 6/input.txt') as f:
    lines = f.readlines()
    start = None
    for i, row in enumerate(lines):
        for j, pos in enumerate(row):
            if pos in '<>^v':
                start = (i, j, pos)
                break
        if start != None:
            break
            
lines = [[x for x in l.strip('\n')] for l in lines]
visited = []

i = start[0]
j = start[1]
pos = start[2]
while not (i, j, pos) in visited:
    visited.append((i, j, pos))
    lines[i][j] = 'X'

    ii = i + step[pos][0]
    jj = j + step[pos][1]

    if ii == -1 or jj == -1 or ii == len(lines) or jj == len(lines[0]):
        break
    elif lines[ii][jj] == '#':
        pos = turn[pos]
    else:
        i, j = ii, jj

tot = 0
for l in lines:
    tot += l.count('X')
    print(''.join(l))
print(tot)
        
