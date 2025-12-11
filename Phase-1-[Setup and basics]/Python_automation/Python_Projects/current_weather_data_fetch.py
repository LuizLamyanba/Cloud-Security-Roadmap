import sys
import json
import requests

API_id = '48f3bbc1a39fedb62be42093645a309f'
if len(sys.argv) < 2 :
    print("Usage:  current_weather_data_fetch.py , location ")
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=%s'% (location, API_id)
response = requests.get(url)
response.raise_for_status()


jsondata = response.json()

if jsondata["cod"] != 200:
    print("City not found!")
    sys.exit()


temp = jsondata["main"]["temp"]
humidity = jsondata["main"]["humidity"]
desc = jsondata["weather"][0]["description"]
city = jsondata["name"]

print("Current weather in %s:" % city)
print("Temperature: %s°C" % temp)
print("Humidity: %s%%" % humidity)
print("Condition: %s" % desc)
















