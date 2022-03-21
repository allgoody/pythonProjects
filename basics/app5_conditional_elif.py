x = input('enter your number:')
x = float(x)
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
elif x < 20 :
    print('big')
elif x < 50 :
    print('large')
elif x < 100 :
    print('huge')
else :
    print('ginormous')
print('all done')