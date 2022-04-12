# 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter your URL:')
html = urllib.request.urlopen(url).read()
soupObject = BeautifulSoup(html, 'html.parser')

#get all of the <a> tags
counts = 0
tags = soupObject('a')
for tag in tags:
    print(tag.get('href',None))
