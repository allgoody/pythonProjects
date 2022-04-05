# file handele open for read be like SEQUENCE of STRINGS/LINES

xfile = open('./test_data/mbox-short.txt','r')

count = 0
for cheese in xfile:
    #print(cheese)    # this will print all the lines in the file!
    count = count + 1
print('Line count:',count)