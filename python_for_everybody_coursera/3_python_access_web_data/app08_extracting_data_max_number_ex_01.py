# + and * are greedy and will take max
# we need to use ? to make it non greedy
# () parenthasis are not part of the match , 
# they tell where to start and stop extraction

import re

hand = open('./test_data/mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:',max(numlist))