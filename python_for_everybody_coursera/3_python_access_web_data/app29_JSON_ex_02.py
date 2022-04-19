import json

# this is list with 2 dictionaries in it
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info)) # <-- we can do len bc this is a list []

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])