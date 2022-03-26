# a function takes some input and produces output

fruit = 'banana'

x = len(fruit)
print(x)

i = 0
while i < len(fruit) : # using while
    w = fruit[i]
    print(i, w)
    i = i + 1

for letter in fruit :     # using for
    print(letter)