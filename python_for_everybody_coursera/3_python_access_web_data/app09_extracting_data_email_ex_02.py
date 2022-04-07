# + and * are greedy and will take max
# we need to use ? to make it non greedy
# () parenthasis are not part of the match , 
# they tell where to start and stop extraction

import re

hand = open('./test_data/mbox-short.txt')
#numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[a-zA-Z0-9-_.]+@[a-zA-Z0-9.]+[a-zA-z]+',line)
    if len(stuff) != 1 : continue # if len(stuff) is empty (!=1) keep looking
    # else print
    print(stuff)
#print(numlist)