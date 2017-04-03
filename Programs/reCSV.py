import os, sys, csv

csvFile = open('test.csv')
data = csv.reader(csvFile)


lastSet = 'Alabama'
index = 0
reorg = []
reorg.append(lastSet)
counties = []
recorder = ''
totalList = []


for row in data:
    setname = row[1]

    if setname != lastSet:
        index += 1
        reorg.append(setname)
        counties.append(recorder)
        recorder = ''

    if len(recorder) == 0:
        recorder = row[0]
    else:
        recorder += ' and '
        recorder += row[0]

    lastSet = setname

counties.append(recorder)

csvOut1 = open('reOrg.csv', 'w', newline='')
csvReOrg = csv.writer(csvOut1)

for each in reorg:
    csvReOrg.writerow(each)

csvOut1.close()

csvOut2 = open('countiesFile.csv', 'w', newline='')
csvCounties = csv.writer(csvOut2)

for each in counties:
    csvCounties.writerow(each)

csvOut2.close()
