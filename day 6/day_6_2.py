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

original_lines = [l.copy() for l in lines]
loops = 0
for i_o in range(len(lines)):
    print(f"{i_o} of {len(lines)}")
    for j_o in range(len(lines[i_o])):
        i = start[0]
        j = start[1]
        pos = start[2]
        visited = []
        lines = [l.copy() for l in original_lines]
        if (i_o == i and j_o == j) or lines[i_o][j_o] == '#':
            continue
        else:
            lines[i_o][j_o] = '#'

        is_loop = 1

        lines[i][j] = '.'
        while not pos in lines[i][j]:
            lines[i][j] += pos

            ii = i + step[pos][0]
            jj = j + step[pos][1]

            if ii == -1 or jj == -1 or ii == len(lines) or jj == len(lines[0]):
                is_loop = 0
                break
            elif lines[ii][jj] == '#':
                pos = turn[pos]
            else:
                i, j = ii, jj
        loops += is_loop

tot = 0
print(loops)
        
