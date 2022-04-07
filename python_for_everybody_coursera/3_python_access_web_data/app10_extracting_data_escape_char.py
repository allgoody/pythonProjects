# \ to escape special character
import re

hand = open('./test_data/mbox-short.txt')
x = 'we just received $10.00 for cookies'
y = re.findall('\$[0-9.]+',x) # \$ looking for literal $ in string
# instead of ($  - matches the end of the line)
print(type(y))