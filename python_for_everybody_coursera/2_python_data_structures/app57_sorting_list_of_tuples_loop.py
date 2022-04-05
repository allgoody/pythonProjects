#  sorted() based on KEYS

d = {'a':10, 'c':1, 'b':22}
t = sorted(d.items())
print(t)

for k,v in sorted(d.items()):
    print(k,v)