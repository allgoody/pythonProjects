# 

import re

hand = open('./test_data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line): # ^ line starts with X and . any char * any number of times
        print(line)