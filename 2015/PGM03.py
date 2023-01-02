#solution for https://adventofcode.com/2015/day/3
instruction = open('../DATA/input03.txt','r').readline()
moves      = {'<':(-1,0), '>':(1,0), '^':(0,1), 'v':(0,-1)}

def run_instruction(move):
    new = (house['last'][0]+moves[move][0], house['last'][1]+moves[move][1])
    house['last'] = new
    return new

######################### PART 1 #########################
house              = {'last': (0,0)}
visited       = [(0,0)]+list(map(run_instruction, instruction))
print('SOLUTION 03a: ', len(set(visited)))

######################### PART 2 #########################
house              = {'last': (0,0)}
visited_santa = [(0,0)]+list(map(run_instruction, instruction[0::2]))
house              = {'last': (0,0)}
visited_robo  = [(0,0)]+list(map(run_instruction , instruction[1::2]))
print('SOLUTION 03b: ', len(set(visited_santa) | set(visited_robo)))

