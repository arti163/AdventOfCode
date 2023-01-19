import json

dok = json.load(open('../DATA/input12.txt', 'r'))

def parse_doc(root):
    typ = type(root)
    s_d, s_l = 0, 0
    if typ == dict:
        for k in root:
            s_d += parse_doc(root[k])
    elif typ == list:
        for k in root:
            s_l += parse_doc(k)
    elif typ == int:
        return s_d + s_l + root
    return s_d + s_l

def parse_doc_red(root):
    typ = type(root)
    s_d, s_l = 0, 0
    if typ == dict:
        if 'red' not in root.keys() and 'red' not in root.values():
            for k in root:
                s_d += parse_doc_red(root[k])
    elif typ == list:
        for k in root:
            s_l += parse_doc_red(k)
    elif typ == int:
        return s_d + s_l + root
    return s_d + s_l

######################### PART 1 #########################
s1 = parse_doc(dok)
print('SOLUTION 12a: ', s1)
######################### PART 2 #########################
s2 = parse_doc_red(dok)
print('SOLUTION 12b: ', s2)