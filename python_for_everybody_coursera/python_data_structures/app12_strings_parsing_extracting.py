# 

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos) # <--with the second parameter it searches first space from atpos
print(sppos)

host = data[atpos+1 : sppos]
print(host)
