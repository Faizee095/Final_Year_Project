import json
from pathlib import Path

path = Path(__file__).parent / \
        "../../subsidiaries/components/settings/user-settings.json"

mydict = {}
mydict["name"] = "Sumit"
print(mydict)
with open(path, 'w') as json_file:
        json.dump(mydict, json_file)
        print("Done")
