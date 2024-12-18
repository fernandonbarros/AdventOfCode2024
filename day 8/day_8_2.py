def get_nodes(a):
    n = []
    for i in range(len(a)):
        a1 = a[i]
        for j in range(i+1, len(a)):
            print(i, j)
            a2 = a[j]
            di = a2[0] - a1[0]
            dj = a2[1] - a1[1]
            n1 = (a1[0] - di, a1[1] - dj)
            n2 = (a2[0] + di, a2[1] + dj)
            n += [n1, n2]

    return n


def get_nodes2(a, height, width):
    n = []
    for i in range(len(a)):
        a1 = a[i]
        for j in range(i+1, len(a)):
            a2 = a[j]
            di = a2[0] - a1[0]
            dj = a2[1] - a1[1]
            k = 0

            while True:
                temp = []

                n1 = (a1[0] - k*di, a1[1] - k*dj)
                n2 = (a2[0] + k*di, a2[1] + k*dj)

                if (n1[0] >= 0 and n1[0] < height) and (n1[1] >= 0 and n1[1] < width):
                    temp.append(n1)
                
                if (n2[0] >= 0 and n2[0] < height) and (n2[1] >= 0 and n2[1] < width):
                    temp.append(n2)

                if temp == []:
                    break
                n += temp
                k += 1

    return n

def print_map(nodes, ants):
    to_print = [[c for c in row] for row in nodes]
    for f in ants:
        for i, j in ants[f]:
            to_print[i][j] = f

    for l in to_print:
        print(''.join(l))

def parse_input(fname):
    with open(f"day 8/{fname}") as f:
        lines = f.readlines()
        lines = [l.strip('\n') for l in lines]

    ants = {}
    h = len(lines)
    w = len(lines[0])

    nodes = [['.' for _ in range(w)] for _ in range(h)]

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c != '.':
                if c in ants:
                    ants[c].append((i, j))
                else:
                    ants[c] = [(i, j)]
    return ants, nodes, h, w


ants, nodes, h, w = parse_input('input.txt')
print_map(nodes, ants)

ns = set()

for freq in ants:
    n = get_nodes2(ants[freq], h, w)
    ns = ns.union(n)

tot = 0
for n in ns:
    nodes[n[0]][n[1]] = 'x'
    tot += 1

print(tot)