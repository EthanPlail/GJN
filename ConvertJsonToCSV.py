import csv, os, sys, json

with open('Gcontent.json') as dataFile:
    data = json.load(dataFile)

csvFile = open('GcontentCSV.csv', 'w')
Fwriter = csv.writer(csvFile)

for wd in data.keys():
    for outerJob in data[wd].keys():
        for innerJob in data[wd][outerJob].keys():
            for i, wage in enumerate(data[wd][outerJob][innerJob].values()):
                if i == 0:
                    code = wage
                elif i == 1:
                    theWage = wage
                elif i == 2:
                    position = wage

            appendList = [wd,outerJob[:5],code,position,theWage]
            Fwriter.writerow(appendList)
