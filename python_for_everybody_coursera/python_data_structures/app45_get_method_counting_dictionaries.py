# x = counts.get(name,0) will look up key in dictionary 
# and add ney key with default value
# <-- name is the key and 0 is the default value
# doesn't traceback

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)