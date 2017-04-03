import requests, sys

yesList = []

for i in range(1000,10000):
    url = 'https://www.wdol.gov/wdol/scafiles/std/17-' + str(i) + '.txt?v=1'
    request = requests.get(url)
    if request.status_code == 200:
        yesList.append(i)
    else:
        a = 5

print(yesList)
