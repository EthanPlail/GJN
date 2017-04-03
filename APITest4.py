### this program will return a list of matching SCA contractors when the zip code and part of the name
### is provided throught the command line
### python3 APITest2.py zipCode Name

import json, requests, sys, xml, untangle
import urllib
import xmltodict

state = str(sys.argv[1])
city = str(sys.argv[2])

key = '043b08a0-8e1e-4a0c-aa74-0c717c26585f'


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
