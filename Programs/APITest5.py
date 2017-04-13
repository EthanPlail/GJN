### this program will return a list of matching SCA contractors when the zip code and part of the name
### is provided throught the command line
### python3 APITest2.py zipCode Name

import json, requests, sys, xml, untangle
import urllib
import xmltodict

import os

from smartystreets_python_sdk import StaticCredentials, exceptions
from smartystreets_python_sdk.us_zipcode import ClientBuilder, Lookup

county = "PLYMOUTH"
city = 'Abington'

key = '##'


url = 'https://us-extract.api.smartystreets.com/?'
			+ auth-id=YOUR_AUTH_ID&
			+ auth-token=YOUR_AUTH_TOKEN
    -H 'Content-Type: text/plain'
	--data-binary '
		There are addresses everywhere.
		1109 Ninth 85007
		SmartyStreets can find them.
		3785 Las Vegs Av.
		Los Vegas, Nevada
		That is all.'


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
