#solution for https://adventofcode.com/2015/day/5
import re
words = [x.strip() for x in open('../DATA/input05.txt', 'r').readlines()]

######################### PART 1 #########################
regex1 = r".*[aeiou].*[aeiou].*[aeiou].*"
regex2 = r"(.)\1+"
regex3 = r".*(ab|cd|pq|xy).*"

slow = sum([bool(len(re.findall(regex1, sl))) * bool(len(re.findall(regex2, sl))) * bool(True-bool(len(re.findall(regex3, sl)))) for sl in words])
print('SOLUTION 05a: ', slow)

######################### PART 2 #########################
regex1 = r"(..).*\1+"
regex2 = r"(.).\1+"

slow = sum([bool(re.findall(regex1, sl))*bool(re.findall(regex2, sl)) for sl in words])
print('SOLUTION 05b: ', slow)
