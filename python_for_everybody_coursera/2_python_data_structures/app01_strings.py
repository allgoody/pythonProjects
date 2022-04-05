# a string is a sequence of characters
# for strings + means concatenate
# we can convert numbers in string into a number using int()
# [] <--index operator in the brackets

fruit = 'banana'
letter = fruit[0]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

length = len(fruit) # !!! <-- gives us 6
i = 0
while i < length :  # from 0-5 < 6 LOL
    print(fruit[i])
    i = i + 1
print('done')
