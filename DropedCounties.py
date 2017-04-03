import os, sys, csv

cwd = os.getcwd()
path = os.path.join(cwd,'WD')

csvFile = open('united-states-counties-removed.csv', 'r')
csvData = csv.reader(csvFile)

csvFile2 = open('state-county-wd2.csv', 'r')
csvWriter = csv.reader(csvFile2)

Dropped = open('Dropped-Counties.csv', 'w')
DroppedWriter = csv.writer(Dropped)

newList = []
newList2 = []

for each in csvData:
    newList.append([each[1].lower(),each[0].lower()[:-1]])

for row in csvWriter:
    newList2.append([row[0].lower(),row[1].lower()])

temp3 = [item for item in newList if item not in newList2]
for area in temp3:
    DroppedWriter.writerow([area[1],area[0]])
    print(area)

csvFile.close()
csvFile2.close()
Dropped.close()
