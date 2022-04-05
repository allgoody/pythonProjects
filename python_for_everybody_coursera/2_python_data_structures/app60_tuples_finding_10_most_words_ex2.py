#  list comprehension creates a dynamic list
# list as expression!

fhand = open('./test_data/romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

lst = sorted( [ (v,k) for k,v in counts.items() ], reverse=True )

for val,key in lst[:10]:
    print(key,val)