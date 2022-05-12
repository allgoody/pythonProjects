#

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# if you have google palaces api key
# enter it here
# api_key = 'ghjkjhjjhlkjhlkj'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"
    
# etails for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('./test_data/geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open('./test_data/where.data')
count = 0
for line in fh:
    if count > 200:
        print('Retrived 200 lacations, restart to retrieve more')
        break
    
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address = ?", (memoryview(address.encode()),))
    
    try:
        data = cur.fetchone()[0]
        print("found in database",address)
        continue
    except:
        pass
    
    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    
    print('Retriveing', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n',' '))
    count = count + 1
    
    try:
        js = json.loads(data)
    except:
        print(data) # in case unicode causes and error
        continue
    
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO RESULTS'):
        print('===Failure to retrieve===')
        print(data)
        break
    
    cur.execute('''INSERT INTO Locations (address,geodata)
                VALUES (?,?)''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)
        
print('Run geomap.py to read the data from database so you can visualize it on a map')
