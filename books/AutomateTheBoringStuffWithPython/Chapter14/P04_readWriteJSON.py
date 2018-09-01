# This program uses the json module to manipulate JSON data

import json

# Reading JSON with the loads() Function
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,' \
                   '"felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

# Writing JSON with the dumps() Function
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
               'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
