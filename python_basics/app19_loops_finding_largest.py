# finding largest value

largest_so_far = None
print('Before', largest_so_far)
for num in [9, 41, 12, 3, 74, 15] :
    if largest_so_far is None :
        largest_so_far = num
    elif largest_so_far < num :
        largest_so_far = num
    print(largest_so_far, num)

print('After', largest_so_far)