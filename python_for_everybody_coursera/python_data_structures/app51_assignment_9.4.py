#

name = input("Enter file:")
if len(name) < 1:
    name = "./test_data/mbox-short.txt"

handle = open(name)

counts = dict()

for line in handle :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = (words[1])
    counts[email] = counts.get(email, 0) + 1

email_count = None
email_most = None
for email,count in counts.items():
    if email_count is None or count > email_count:
        email_most = email
        email_count = count

# all done
print(email_most, email_count)
