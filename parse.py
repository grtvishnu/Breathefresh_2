import requests
import json


f = open('measurements.json', "r")

data = json.loads(f.read())

# for city in data['results'] == "Harjumaa":

#     print(city)


# print(json.dumps(data['city'], indent=4, separators=(". ", " = ")))
# Harjumaa


# output_dict = [f for f in data if f['city'] == 'Harjumaa']


# output_json = json.dumps(output_dict)

# print(output_json)
