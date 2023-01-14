######################### PART 1 #########################
diff = sum([len(x.strip())- len(eval(x.strip())) for x in open('../DATA/input08.txt', 'r').readlines()])
print('SOLUTION 08a: ', diff)

######################### PART 1 #########################
diff = sum([(x.strip().count('\\') + (x.strip().count('\"')) + 2) for x in open('../DATA/input08.txt', 'r').readlines()])
print('SOLUTION 08b: ', diff)
