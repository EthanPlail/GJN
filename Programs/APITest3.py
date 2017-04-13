### this program will return a list of matching SCA contractors when the zip code and part of the name
### is provided throught the command line
### python3 APITest2.py zipCode Name

#import json, requests, sys, xml, untangle
#import urllib
#import xmltodict
import python_usdol

conn = python_usdol.Connection(token="##", secret="##")

data = conn.fetch_data("FORMS", "AgencyForms", filter_="AgencyId eq 'MSHA'")

#location = str(sys.argv[1])
#company = str(sys.argv[2])


#url = "http://api.dol.gov/V1/FORMS/AgencyForms?$filter=(AgencyId eq 'MSHA') and (Title eq 'Legal Identity Report')"
#response = urllib.request.urlopen(url)

#response.close()

print(data.read())


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
