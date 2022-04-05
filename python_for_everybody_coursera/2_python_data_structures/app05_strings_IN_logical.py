# IN could be used to check if string in another string
#it returns True or False and can be used in IF statement

fruit = 'banana'
if 'a' in fruit :
    print('found it!')

count = 0
for i in fruit :
    if i == 'a' :
        count = count + 1


w = 'n' in fruit
s = 'z' in fruit

print(count, '\n',w, '\n',s)
