#solution for https://adventofcode.com/2015/day/1
instructions = open('../DATA/input01.txt', 'r').readline()

######################### PART 1 #########################
print('SOLUTION 01a: ', instructions.count('(') - instructions.count(')'))

######################### PART 2 #########################
floors = [instructions[:idx+1].count('(')-instructions[:idx+1].count(')') for (idx,x) in enumerate(instructions)]
print('SOLUTION 01b: ', floors.index(-1)+1)