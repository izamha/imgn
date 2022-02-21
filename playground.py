import json

json_data = open('./imigani.json')
dta = json.load(json_data)

print(json.dumps(dta))
