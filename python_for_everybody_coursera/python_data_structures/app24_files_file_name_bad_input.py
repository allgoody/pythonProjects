# 

fname = input('enter path to file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('there were',count, 'subject lines in',fname)
