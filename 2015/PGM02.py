#solution for https://adventofcode.com/2015/day/2
presents = [list(map(int, x.strip().split('x'))) for x in open('../DATA/input02.txt','r').readlines()]

######################### PART 1 #########################
paper = sum([2*x[0]*x[1]+2*x[0]*x[2]+2*x[1]*x[2]+sorted(x)[0]*sorted(x)[1] for x in presents])
print('SOLUTION 02a: ', paper)

######################### PART 2 #########################
ribbon = sum([x[0]*x[1]*x[2]+2*sorted(x)[0]+2*sorted(x)[1] for x in presents])
print('SOLUTION 02a: ', ribbon)
