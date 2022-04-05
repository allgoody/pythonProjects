# 

counts = dict()
print('Enter a line of text:')
line = input('')
#line = open('./test_data/mbox-short.txt')

words = line.split()
print('Words:', words)

print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)