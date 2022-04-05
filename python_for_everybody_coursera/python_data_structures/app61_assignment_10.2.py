# 

name = input("Enter file:")
if len(name) < 1:
    name = "./test_data/mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    colon = line.find(':')
    hour = line[colon-2:colon-0]
    counts[hour] = counts.get(hour,0) + 1

lst = list()
for key,val in counts.items():
    tup = (key,val)
    lst.append(tup)

lst = sorted(lst)

for key, val in lst:
    print(key,val)