chain = open('../DATA/input10.txt','r').readline().strip()

def create_chain(elements):
    chain = ''
    for el in elements:
        chain += str(el[0])+el[1]
    return chain

for i in range(50):
    prev = chain[0]
    idx = [1]
    for el in chain[1:]:
        if el == prev:
            idx.append(idx[-1]+1)
        else:
            idx.append(1)
        prev = el

    elements = [(idx[i], chain[i]) for i in range(len(idx)-1) if idx[i]>=idx[i+1]]
    elements.append((idx[-1], chain[-1]))

    chain = create_chain(elements)
    
    if i+1 == 40:
        solution_a = len(chain)
    if i+1 == 50:
        solution_b = len(chain)

######################### PART 1 #########################
print('SOLUTION 10a: ', solution_a)

######################### PART 2 #########################
print('SOLUTION 10b: ', solution_b)
