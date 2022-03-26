# : (colon operator) sets range and goes up to BUT not included !!!


s = 'monty python' # range 0-11
print(s[0:4])      # from 0 to 3 (4 not included)

print(s[6:7])      # from 6 to 7 (7 not included)

print(s[6:20])  # out of range - stops at the end

print(s[:2])    # from 0 to 2, 2 not included

print(s[8:])    # from 8 to the end

print(s[:])     # from 0 to the end
