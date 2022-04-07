# 

import re

hand = open('./test_data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):  # ^ - matches the beginning of line
        print(line)