# JSON represents data as nested lists and dictionaries
# we get object as Python dictionary

import json
data = '''[ "Glenn", "Sally", "Jen" ]'''

info  = json.loads(data) # <-- info is dictionary
print(type(info))