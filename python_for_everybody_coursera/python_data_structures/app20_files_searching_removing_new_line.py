# we can read the whole file ( new lines etc ) into a single string

fhand = open('./test_data/mbox-short.txt')

for line in fhand :
    line = line.rstrip()   # <-- strips line from \n character
    if line.startswith('From:') :
        print(line)
