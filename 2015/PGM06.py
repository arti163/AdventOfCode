#solution for https://adventofcode.com/2015/day/6
import numpy as np

instructions = [(x.strip().split()[0], x.strip().split()[1], x.strip().split()[3]) 
                    if len(x.strip().split()) == 4 
                    else (x.strip().split()[1], x.strip().split()[2], x.strip().split()[4]) 
                        for x in open('../DATA/input06.txt', 'r').readlines()]
SIZE = 1000
turn_A = {'on' : 1, 'off': 0}
turn_B = {'on' : 1, 'off': -1, 'toggle' : 2}

def run_instructions_stepA(instr):
    (ax, ay) = map(int, instr[1].strip().split(','))
    (bx, by) = map(int, instr[2].strip().split(','))
    
    if instr[0] == 'toggle':
        grid[ax:bx+1, ay:by+1] = 1 - grid[ax:bx+1, ay:by+1]
        return instr[0]
    else:
        grid[ax:bx+1, ay:by+1] = turn_A[instr[0]]
        return instr[0]

def run_instructions_stepB(instr):
    (ax, ay) = map(int, instr[1].strip().split(','))
    (bx, by) = map(int, instr[2].strip().split(','))

    grid[ax:bx+1, ay:by+1] = grid[ax:bx+1, ay:by+1] + turn_B[instr[0]]
    grid[grid<0] = 0
    return instr[0]

######################### PART 1 #########################
grid = np.zeros((SIZE, SIZE))
list(map(run_instructions_stepA, instructions))
print('SOLUTION 06a: ', int(sum(sum(grid))))

######################### PART 2 #########################
grid = np.zeros((SIZE, SIZE))
list(map(run_instructions_stepB, instructions))
print('SOLUTION 06b: ', int(sum(sum(grid))))