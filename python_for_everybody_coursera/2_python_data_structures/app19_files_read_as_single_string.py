# we can read the whole file ( new lines etc ) into a single string

fhand = open('./test_data/mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

for line in fhand :
    if line.startswith('From:') :
        print(line)