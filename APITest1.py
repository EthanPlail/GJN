import json, requests, sys

location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=61a4ad4f4c2e843a2a3058bc00756610' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
