### this program will return a list of matching SCA contractors when the zip code and part of the name
### is provided throught the command line
### python3 APITest2.py zipCode Name

import json, requests, sys, xml, untangle
import urllib
import xmltodict

location = str(sys.argv[1])
company = str(sys.argv[2])


url = 'https://www.usaspending.gov/fpds/fpds.php?detail=l&fiscal_year=2017&placeOfPerformanceZIPCode=' + location + '&company_name=' + company
response = urllib.request.urlopen(url)
data = response.read()
response.close()

data = xmltodict.parse(data)

parseData = data['usaspendingSearchResults']['data']['records']['record']

for each in parseData:
    print(each['mod_parent'])


#
# testdata = data[1]
# print each in testdata:
#
#
# for each in data.values():
#     print(each)

# contractData = ET.parse(response)
# root = contractData.getroot()
#
# root = ET.fromstring(response_as_string)
#
# for child in root:
#     print(child.tag, child.attrib)
