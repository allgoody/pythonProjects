# JSON represents data as nested lists and dictionaries
# we get object as Python dictionary

import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
    }'''

info  = json.loads(data) # <-- info is dictionary
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
print('Phone',info["phone"]["number"])