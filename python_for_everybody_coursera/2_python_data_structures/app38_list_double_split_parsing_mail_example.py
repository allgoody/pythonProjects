#  

fhand = open('./test_data/mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split() # split based on spaces
    email = words[1]
    pre_domain = email.split('@')
    domain = pre_domain[1]
    print(domain) 
