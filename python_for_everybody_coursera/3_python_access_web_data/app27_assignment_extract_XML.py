import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dataUrl = input('Enter data URL:')
dataOpen = urllib.request.urlopen(dataUrl, context=ctx).read().decode()

dataTree = ET.fromstring(dataOpen)
commentCount = dataTree.findall('comments/comment')

commentSum = 0
for count in commentCount :
    i = count.find('count').text
    commentSum = commentSum + int(i)
print('The sum of all comments is:',commentSum)