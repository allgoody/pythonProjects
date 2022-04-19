# 

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dataUrl = input('Enter data URL:')
dataOpen = urllib.request.urlopen(dataUrl, context=ctx).read().decode()

dataJson = json.loads(dataOpen)
# print(json.dumps(dataJson, indent=4))

# commentSum = 0
# for item in dataJson['comments']:
#     i = int(item['count'])
#     commentSum = commentSum + i
# print(commentSum)

print( sum ( [int(item['count']) for item in dataJson['comments'] ]))