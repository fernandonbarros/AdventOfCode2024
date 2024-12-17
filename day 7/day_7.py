def eval_test(tot, vals, cur=0, ops='', concatenate=False):
    if vals == []:
        return cur == tot
    
    # if cur >= tot:
    #     return False
    valid = eval_test(tot, vals[1:], cur*vals[0], ops+'*', concatenate)
    valid = valid or eval_test(tot, vals[1:], cur+vals[0], ops+'+', concatenate)
    if concatenate:
        valid = valid or eval_test(tot, vals[1:], int(f"{cur}{vals[0]}"), ops+'|', concatenate)
    return valid


with open('day 7/input.txt') as f:
    tests = []
    for l in f.readlines():
        result, vals = l.strip('\n').split(':')
        tests.append((int(result), [int(v) for v in vals.strip(' ').split(' ')]))

final = 0
final_concat = 0
i = 0
for t in tests:
    i += 1
    print(f"{i} of {len(tests)}")
    tot = t[0]
    vals = t[1]

    valid = eval_test(tot, vals)
    final += tot*valid

    valid = eval_test(tot, vals, concatenate=True)
    final_concat += tot*valid

print(f"Part 1 = {final}")
print(f"Part 2 = {final_concat}")
