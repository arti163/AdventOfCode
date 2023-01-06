#solution for https://adventofcode.com/2015/day/7
actions = {'AND': '&', 'OR': '|', 'XOR': '^', 'NOT': '~', 'LSHIFT' : '<<', 'RSHIFT': '>>'}
values_ = dict()
operations = dict()

def read_instruction(lancuch):
    (components, result) = lancuch.strip().split(' -> ')
    components = components.strip().split(' ')
    if len(components) == 1:
        d = ((components[0],None), '=')
    if len(components) == 2:
        d = ((components[1],None), actions[components[0]])
    if len(components) == 3:
        d = ((components[0], components[2]), actions[components[1]])
    operations[result] = d

def get_components(component):
    (lh, rh) = component
    if str(lh).isnumeric():
        lh = int(lh)
    if str(rh).isnumeric():
        rh = int(rh)
    lh = values_.get(lh, lh)
    rh = values_.get(rh, rh)
    return (lh, rh)

def perform_action(dz):
    res = dz
    component = operations[dz][0]
    action = operations[dz][1]
    if res not in values_:
        (lh, rh) = get_components(component)
        if type(lh) == int and (type(rh) == int or rh is None):
            if action in ('&', '|', '^', '<<', '>>'):
                command = '%d%s%d' % (lh, action, rh)
            elif action in ('~'):
                command = '%s%d' % (action, lh)
            else:
                command = '%d' % lh
            values_[res] = eval(command)

######################### PART 1 #########################
_ = [read_instruction(x) for x in open('../DATA/input07.txt','r').readlines()]
while 'a' not in values_:
    list(map(perform_action, operations))
print('SOLUTION 07a: ', values_['a'])

######################### PART 1 #########################
values_ = {'b': values_['a']}
while 'a' not in values_:
    list(map(perform_action, operations))
print('SOLUTION 07b: ', values_['a'])
