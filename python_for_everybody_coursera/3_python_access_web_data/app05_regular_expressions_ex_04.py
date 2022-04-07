# 

import re

hand = open('./test_data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line): # ^ line starts with X- and \S any non-whitespace char + one or more number of times
        print(line)