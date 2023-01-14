import itertools

cts = dict()
ctx = dict()
dst = dict()

def read_line(x):
    x = x.strip().split(' ')
    cf = x[0]
    ct = x[2]
    ds = int(x[4])
    if cf not in cts.values():
        cts[len(cts)] = cf
        ctx[cf] = len(ctx)
    if ct not in cts.values():
        cts[len(cts)] = ct
        ctx[ct] = len(ctx)
    dst[(ctx[cf], ctx[ct])] = ds
    dst[(ctx[ct], ctx[cf])] = ds

def tour_length(route):
    dist = 0
    for i in range(len(route)-1):
        dist += dst[(route[i], route[i+1])]
    return dist

######################### PART 1 #########################
list(map(read_line, open('../DATA/input09.txt', 'r').readlines()))
prms = list(itertools.permutations(range(len(cts))))
shortest = min(list(map(tour_length, prms)))
print('SOLUTION 09a: ', shortest)

######################### PART 2 #########################
longest = max(list(map(tour_length, prms)))
print('SOLUTION 09b: ', longest)
