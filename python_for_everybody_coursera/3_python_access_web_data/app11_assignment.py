# re.findall returns list if nothing will get empty list

import re

num = 0
count = 0
numlist = list()
hand = open('./test_data/regex_sum_1514478.txt')
inp = hand.read()

stuff = re.findall('[0-9]+', inp)
for num in stuff:
    num = int(num)
    numlist.append(num)
    count = count + 1

print(sum(numlist))
print(count)
