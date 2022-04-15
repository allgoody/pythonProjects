# 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
positionCount = input('Enter count:')
positionCount = int(positionCount)
urlPosition = input('Enter url position number:')

while positionCount > 0:
    positionCount = positionCount - 1

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    urlDict = dict()
    count = 0
    tags = soup('a')
    for tag in tags:
        singleUrl = tag.get('href',None)
        count = count + 1
        urlDict[singleUrl] = urlDict.get(singleUrl,count)

    listKeys = list(urlDict.keys())
    listValues = list(urlDict.values())

    url = listKeys[listValues.index(int(urlPosition))]
    print('Retrieving:',url)
    