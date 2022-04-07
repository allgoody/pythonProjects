# re.findall returns list if nothing will get empty list

import re

num = 0
hand = open('./test_data/regex_sum_1514478.txt')

print( sum( [ int(num) for num in re.findall('[0-9]+', hand.read()) ]) )