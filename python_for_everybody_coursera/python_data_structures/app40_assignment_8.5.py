#  

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    count = count + 1
    words = line.split() # split based on spaces
    print(words[1]) #<--prints email from each line

print("There were", count, "lines in the file with From as the first word")
