# removing whitespace at the beginning and/or end
# lstrip() and rstrip() remove whitespaces left or right
# strip() removes both left and right

greet = ' Hello Bob  '
test = '  get a job  '
print(greet.lstrip(),test)
print(greet.rstrip())
print(greet.strip(),test.strip())
