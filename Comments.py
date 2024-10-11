import json
with open("settings.json", "r") as jsonfile:
    jsondata = ''.join(line for line in jsonfile if not line.startswith('//'))
    data = json.loads(jsondata)
print(data)
