#  

fhand = open('./test_data/mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split() # split based on spaces
    print(words[1]) #<--prints email from each line
