import urllib.parse
import requests

main_api = 'http://api.openaq.org/v1/latest?'

city = 'Pune'

while True:
    city = input("Location :")
    url = main_api + urllib.parse.urlencode({'city': city})
    json_data = requests.get(url).json()
    formatted_location = json_data['results'][0]['location']
    print(formatted_location)
    for each in json_data['results'][0]['measurements']:
        print(each['parameter'], each['value'])
