### this program will return a list of matching SCA contractors when the zip code and part of the name
### is provided throught the command line
### python3 APITest2.py zipCode Name

import json, requests, sys, xml, untangle
import urllib
import xmltodict

state = str(sys.argv[1])
city = str(sys.argv[2])

key = '##'


url = 'http://api.dol.gov/V1/WHPS/?KEY=' + key
response = urllib.request.urlopen(url)
data = response.read()
response.close()

data = xmltodict.parse(data)

print(data)



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
