rules = {}
updates = []

def check_udpate(u, rules):
    prev = set()
    for i in range(len(u)):
        n = u[i]
        if n in rules:
            r = rules[n]
            s = set(u[:i]).intersection(r)
            if len(s) > 0:
                return False
    return True

def sort_update(u, rules):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(u)-1):
            if u[i+1] in rules.get(u[i], set()):
                u[i], u[i+1] = u[i+1], u[i]
                swapped = True

    return u[::-1]

with open('day 5/input.txt') as f:
    lines = f.readlines()
    reading_rules = True
    for l in lines:
        l = l.strip('\n')
        if l == '':
            reading_rules = False
            continue

        if reading_rules:
            k, v = l.split('|')
            k = int(k)
            v = int(v)
            if k in rules:
                rules[k].add(v)
            else:
                rules[k] = set([v])
        else:
            u = [int(n) for n in l.split(',')]
            updates.append(u)
        l = f.readline()

tot = 0
tot_incorrect = 0

for u in updates:
    if check_udpate(u, rules):
        i = len(u) // 2
        tot += u[i]
        # print(u)
    else:
        u_new = sort_update(u, rules)
        i = len(u_new) // 2
        tot_incorrect += u_new[i]
        # print(u_new)


print('Part 1 =', tot)
print('Part 2 =', tot_incorrect)