# find() to search for a substring withing another string
# find() fins first occurrence
#if not found returns -1

fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)
if aa == -1:
     print(aa, 'not found')


input_word = 'banana'
input_letter = 'n'

for input_letter in input_word :
    ltr = input_word.find(input_letter)
    print(ltr)
