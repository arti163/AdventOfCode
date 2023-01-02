#solution for https://adventofcode.com/2015/day/4
import hashlib
secret = open('../DATA/input04.txt', 'r').readline().strip()

######################### PART 1 #########################
hashes = [hashlib.md5((secret+str(x)).encode('utf-8')).hexdigest()[:5] for x in range(1000000)]
print('ROZWIAZANIE 04a: ', hashes.index('00000'))

######################### PART 1 #########################
hashes = [hashlib.md5((secret+str(x)).encode('utf-8')).hexdigest()[:6] for x in range(5000000)]
print('ROZWIAZANIE 04b: ', hashes.index('000000'))

