# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
added = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    find_dot = line.find('.')
    srt_number = line[find_dot-1:find_dot+5]
    float_number = float(srt_number)
    count = count + 1
    added = added + float_number
print('Average spam confidence:', added / count)