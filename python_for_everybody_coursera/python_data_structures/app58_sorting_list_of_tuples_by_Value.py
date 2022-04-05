#  

c = {'a':10, 'c':1, 'b':22}
tmp = list()

for k,v in c.items():
    tmp.append((v,k)) # <--reversing key and value
print(tmp)

tmp = sorted(tmp)
print(tmp)
tmp = sorted(tmp, reverse=True) # reverse sort from big to low
print(tmp)