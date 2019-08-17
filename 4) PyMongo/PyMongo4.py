import json
item = {"first": 123, "second": 456,   "third": {"1": 1,  "2": 2}}
print(json.dumps(item, indent=4, sort_keys=True))
