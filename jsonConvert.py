from json2xml.json2xml import Json2xml
data = Json2xml.fromjsonfile('examples/example.json').data
data_object = Json2xml(data)
data_object.json2xml()
