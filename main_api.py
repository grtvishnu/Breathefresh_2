import urllib.parse
import requests

main_api = 'http://api.openaq.org/v1/latest?'


city = input("Location :")
url = main_api + urllib.parse.urlencode({'city': city})
json_data = requests.get(url).json()
formatted_location = json_data['results'][0]['location']
print(formatted_location)
for each in json_data['results'][0]['measurements']:
    # print(each['parameter'], each['value'])
    if each['parameter'] == 'co':
        co = each['value']
    elif each['parameter'] == 'so2':
        so2 = each['value']
    elif each['parameter'] == 'pm10':
        pm10 = each['value']
    elif each['parameter'] == 'pm25':
        pm25 = each['value']
    elif each['parameter'] == 'o3':
        o3 = each['value']
    elif each['parameter'] == 'no2':
        no2 = each['value']
print("CO :", co)
print("NO2 :", no2)
print("O3 :", o3)
print("PM10 :", pm10)
print("SO2 :", so2)
print("PM2.5 :", pm25)
