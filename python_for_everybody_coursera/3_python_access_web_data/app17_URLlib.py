# 

import urllib.request, urllib.parse, urllib.error
import re

count = 0
fhand = urllib.request.urlopen('https://github.com/allgoody/pythonProjects')
for line in fhand:
    text = line.decode()
    # i = re.findall('.*(about).*',text)
    # if len(i) !=1 :continue
    if 'about' in text:
    # print(i)
        count = count + 1
print(count)