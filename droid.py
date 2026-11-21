import itertools

def first(l,h,min_length=4):
    return itertools.chain(
            itertools.permutations(
                xrange(1,l*h+1), i)
            for i in xrange(min_length,l*h+1))

fst = first(3,3)

def rejector(lst, l,h):
    for idx in xrange(len(lst)-1):
        first, second = itertools.islice(lst, idx, idx+2)
        for num in interpolate(l, h, first, second):
            if num not in itertools.islice(lst, idx):
                print [first, second]
                return False
    return True

def interpolate(l, h, n1, n2):
    #l: row length
    #h: number of rows
    #n1, n2: values to interpolate between
    r1, r2 = sorted([n1-1, n2-1])
    row_diff = (r2 / l) - (r1 / l)
    if row_diff == 0:
        return range(r1+2, r2+1)
    if row_diff == 1:
        return []
    else:
        out = []
        col_diff = (r2 % l - r1 % l)
        for idx in range(1, (r2 / l) - (r1 / l)):
            frac = (1.0 * idx * col_diff / row_diff)
            if int(frac) == frac:
                out.append(r1 + idx*l + int(frac))
        return [x +1 for x in out]
