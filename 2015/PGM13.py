import itertools

acts = dict()
actx = dict()
dst = dict()

def read_lines(x):
    x = x.strip().split(' ')
    a1 = x[0]
    a2 = x[10].replace('.','')
    ds = int(x[3]) if x[2] == 'gain' else -int(x[3])
    if a1 not in acts.values():
        acts[len(acts)] = a1
        actx[a1] = len(actx)
    if a2 not in acts.values():
        acts[len(acts)] = a2
        actx[a2] = len(actx)
    dst[(actx[a1], actx[a2])] = ds

def tour_length(route):
    dist = 0
    for i in range(len(route)):
        dist += dst[(route[i], route[i-1])]+dst[(route[i-1], route[i])]
    return dist

def add_myself():
    if 'Me' not in acts.values():
        acts[len(acts)] = 'Me'
        actx['Me'] = len(actx)
    for a in actx:
        dst[(actx['Me'], actx[a])] = 0
        dst[(actx[a], actx['Me'])] = 0

######################### PART 1 #########################
list(map(read_lines, open('../DATA/input13.txt', 'r').readlines()))
prms = list(itertools.permutations(range(len(acts))))
maximal = max(list(map(tour_length, prms)))
print('SOLUTION 13a: ', maximal)

######################### PART 2 #########################
add_myself()
prms = list(itertools.permutations(range(len(acts))))
maximal = max(list(map(tour_length, prms)))
print('SOLUTION 13b: ', maximal)
