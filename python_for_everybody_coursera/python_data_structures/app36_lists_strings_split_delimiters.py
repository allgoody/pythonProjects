#  if delimiter is not specified - 
# multiple spaces treated like one delimiter
# we can specify delimiter in split function ex: .split(';')

line  = 'A lot         of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))

line = 'Line one\nLine two\nLine three'
new_line = line.split()
print(new_line)

new_line = line.split('\n')
print(new_line)