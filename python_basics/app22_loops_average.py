# counting numbers

sum = 0
count = 0
average = 0
print('sum before the loop', sum)
for i in [9, 41, 6, 45, 22, 67, 9] :
    count = count + 1
    sum = sum + i
    average = sum / count
    print('in step', count, 'sum is', sum, 'and the average is', average)
print('average after the loop', average)