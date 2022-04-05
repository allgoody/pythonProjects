# List [] - a linear collection of values that stay in order
# Dictionary {} - a 'bag' of values, each with its own key (key:value)
# Dictionaries allow us to do fast database-like operations in python

purse = dict()
purse['money'] = 12 # money is the key, 12 is the value
purse['candy'] = 3  # purse sub - candy
purse['tissues'] = 75
print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2

print(purse['candy'])

print(purse)