#  

fname = input("Enter file name: ") # get the file
fh = open(fname) # open portal to the file
lst = list() # create empty main list
for line in fh: # for each line in the file
    line = line.rstrip() # strip from right new line char.
    words = line.split() # split line in list of words
    for word in words: # for each word in the list of words of the line
        if word in lst : continue # look if word alredy in the main list and keep looking if it is
        lst.append(word) # if word is not in the list append it

lst.sort()        # sort from a-z
print(lst)        # print main list
