# conditional statements
# < less than
# <= less or equal
# == equal to
# >= greater than
# != not equal (bang equal)

x = input('Enter your number:')
x = float(x)
if x < 10:
    print('Smaller than 10')
    print('Some more output if less than 10')
    if x == 10:
        print('Equals 10')
    else:
        print('Not equal 10 in equal block')
else: 
    print('Bigger than 10')

if x !=10:
    print('Not equal 10')
