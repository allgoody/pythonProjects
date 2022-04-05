# 

fname = input('enter path to file: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('there were',count, 'subject lines in',fname)
