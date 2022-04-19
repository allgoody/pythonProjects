import urllib.request, urllib.parse, urllib.error
import twurl
import json

Twitter_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('enter twitter account:')
    if (len(acct) < 1): break
    url = twurl.augment(Twitter_URL, {'screen_name': acct, 'count' : '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders()) # getting headers
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['test']
        print(' ', s[:50])