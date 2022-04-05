#

sum = 0
count = 0
avrage = 0
while True :
    snum = input('Enter a number: ')
    if snum == 'done' :
        break
    else :
        try :
            fnum = float(snum)
        except :
            print('Invalid input')
            continue
        sum = sum + fnum
        count = count + 1
        average = sum / count

print('Sum is', sum, 'Count is', count, 'Average is', average)