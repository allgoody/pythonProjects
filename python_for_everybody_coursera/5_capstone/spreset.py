import sqlite3

conn = sqlite3.connect('./test_data/spideer.sqlite')
cur = conn.cursor()

cur.execute('''
UPDATE Pages SET new_rank=1.0, old_rank=0.0
''')
conn.commit()

cur.close()

print("All pages set to rank of 1.0")