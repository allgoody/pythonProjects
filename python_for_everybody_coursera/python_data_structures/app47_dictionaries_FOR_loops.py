# 

counts = {'chuck':1,'fred':42,'jan':100}
for key in counts: # if we put name of the dictionary loop goes through the keys not values
    print(key, counts[key])

print(list(counts)) # list will print keys not values

print(counts.values()) # requesting values only

print(list(counts.values())) # prints list of values

print(counts.items())