# Part 1
def arrangement_count(p, g, springs, groups):
    if g >= len(groups):
        if p < len(springs) and '#' in springs[p:]:
            return 0
        return 1
    
    if p >= len(springs):
        return 0

    res = None
    gs = groups[g]

    if springs[p] == '?':
        if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
            res = arrangement_count(p + gs + 1, g + 1, springs, groups) + arrangement_count(p + 1, g, springs, groups)
        else:
            res = arrangement_count(p + 1, g, springs, groups)
    elif springs[p] == '#':
        if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
            res = arrangement_count(p + gs + 1, g + 1, springs, groups)
        else:
            res = 0
    elif springs[p] == '.':
        res = arrangement_count(p+1, g, springs, groups)

    return res

with open('input.txt') as f:
    sum_of_arrangements = 0

    for line in f.readlines():
        springs, groups = line.split()

        groups = list(map(int, groups.split(',')))
        springs = springs + '.'

        sum_of_arrangements += arrangement_count(0, 0, springs, groups)

    print(sum_of_arrangements)

# Part 2
MEMO = {}

def arrangement_count(p, g, springs, groups):
    if g >= len(groups):
        if p < len(springs) and '#' in springs[p:]:
            return 0
        return 1
    
    if p >= len(springs):
        return 0

    if (p, g) in MEMO: return MEMO[(p, g)]

    res = None
    gs = groups[g]

    if springs[p] == '?':
        if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
            res = arrangement_count(p + gs + 1, g + 1, springs, groups) + arrangement_count(p + 1, g, springs, groups)
        else:
            res = arrangement_count(p + 1, g, springs, groups)
    elif springs[p] == '#':
        if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
            res = arrangement_count(p + gs + 1, g + 1, springs, groups)
        else:
            res = 0
    elif springs[p] == '.':
        res = arrangement_count(p+1, g, springs, groups)

    MEMO[(p, g)] = res
    return res

with open('input.txt') as f:
    sum_of_arrangements = 0

    for line in f.readlines():
        springs, groups = line.split()
       
        springs = "?".join([springs] * 5)
        springs = springs + '.'
        groups = list(map(int, groups.split(','))) * 5

        MEMO = {}
        sum_of_arrangements += arrangement_count(0, 0, springs, groups)

    print(sum_of_arrangements)
