# import re - to import python regex library

# re.search() - to see if a string matches a regex

# re.findall() - to extract portions of a string that matches regular expression

import re

hand = open('./test_data/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)