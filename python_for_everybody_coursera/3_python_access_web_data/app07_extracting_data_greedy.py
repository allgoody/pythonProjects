# + and * are greedy and will take max
# we need to use ? to make it non greedy

import re

x = 'From: Using the : character'
y = re.findall('^F.+?:',x) 
print(y)