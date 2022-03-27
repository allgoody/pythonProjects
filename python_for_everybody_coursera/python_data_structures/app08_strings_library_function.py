# these functions built into every string,
# INVOKE them by appending the function to the string variable
# these functions do not modify the original string
# instead they return a new string that has been altered
# DIR will show methods in class STR (string)

greet = 'Hello Bob'
alt_low = greet.lower() # <-- object method
print(alt_low)
print(greet)

print('Hi There'.lower())

print(type(greet))
print(dir(greet))

print(greet.upper())
print(greet.swapcase())
