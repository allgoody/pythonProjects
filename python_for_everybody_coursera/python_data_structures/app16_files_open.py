# open() function returns a file handle - a variable used to perform operation on the file
# handle = open(filename,mode) eg: fhand = open('mbox.txt','r')
# filename is a string
# mode is optional and should be 'r' if we want to read the file
# and 'w' if we are going to write to the file
# mode is 'r' by default

fhand = open('./test_data/mbox-short.txt','r')
print(fhand)

stuff = 'Hello\nWorld!'
print(stuff)

stuff = "X\nY"
print(stuff)

print(len(stuff))