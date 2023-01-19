chain = open('../DATA/input11.txt','r').readline().strip()

letters = 'abcdefghijklmnopqrstuvwxyz'

MAX_IDX = len(letters)
r1_letters = [letters[i:i+3] for i in range(len(letters)-2)]
r2_letters = ['i', 'o', 'l']
r3_letters = [x*2 for x in letters]

def test(chain):
    w1 = max([x in chain for x in r1_letters])
    w2 = not max([x in chain for x in r2_letters])
    w3 = sum([x in chain for x in r3_letters]) >= 2
    return w1 & w2 & w3

def generate_chain(number):
        str26n = ''
        for i in range(7,-1,-1):
            w = int(number/(MAX_IDX**i))
            str26n += letters[w]
            number = number-w*(MAX_IDX**i)
        return str26n

def generate_password(chain):
    L26 = sum([letters.index(z)*(MAX_IDX**i) for (i, z) in enumerate(chain[::-1])])
    inc, L26n = 0, 0
    str26n = chain
    while not test(str26n):
        inc += 1
        L26n = L26+inc
        str26n = generate_chain(L26n)
    return str26n, L26n

######################### PART 1 #########################
password_p1, number_p1 = generate_password(chain)
print('SOLUTION 11a: ', password_p1)
######################### PART 1 #########################
chain = generate_chain(number_p1+1)
password_p2, number_p2 = generate_password(chain)
print('SOLUTION 11b: ', password_p2)