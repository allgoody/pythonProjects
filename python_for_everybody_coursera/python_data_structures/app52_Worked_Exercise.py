#

fname = input('enter file:')
if len(fname) < 1 : fname = './test_data/intro.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds :
        w = w.strip('.').strip(')').strip('?')
        w = w.strip(',')
        di[w] = di.get(w,0) + 1

#print(di)

largest = 0
theword = None
for k,v in di.items() :
    #print(k,v)
    if v > largest :
        largest = v
        theword = w

print(theword, largest)
