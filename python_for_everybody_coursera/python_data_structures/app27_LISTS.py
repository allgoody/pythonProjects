# algorithms - a set of rules or steps used to solve a problem
# Data structures - a particular way of organizing data
# Elements in a list are separated by commas
# A list element can be any python object - even another list
# List can be empty

print([1,[5,6],7])

print([])

friends = ['Joseph',"Glenn","Sally"] # <-- list starts with 0
print(friends[1])

lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 123
print(lotto)

lotto_1 = [2,14,26,41,63]
print(lotto_1)
lotto_1[2] = [3,7,8,98]
print(lotto_1)
print(len(lotto_1))

print(range(4)) # <-- Range function -
# - returns a list of numbers starts with 0 to one less than parameter

print(range(len(friends)))

for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year:', friend)