import os, csv

DataFile = open('GcontentCSV2.csv','r')
Data = csv.reader(DataFile)

count = 0

firstLine = ['WD','Area','Wage','Name','Code']

file20 = open('./SplitContent/WDcontent20.csv','w')
file40 = open('./SplitContent/WDcontent40.csv','w')
file60 = open('./SplitContent/WDcontent60.csv','w')
file80 = open('./SplitContent/WDcontent80.csv','w')
file100 = open('./SplitContent/WDcontent100.csv','w')

writer20 = csv.writer(file20)
writer40 = csv.writer(file40)
writer60 = csv.writer(file60)
writer80 = csv.writer(file80)
writer100 = csv.writer(file100)

writer20.writerow(firstLine)
writer40.writerow(firstLine)
writer60.writerow(firstLine)
writer80.writerow(firstLine)
writer100.writerow(firstLine)

for each in Data:
    if int(each[0]) <= 4295:
        writer20.writerow(each)
    elif int(each[0]) <= 4683:
        writer40.writerow(each)
    elif int(each[0]) <= 5045:
        writer60.writerow(each)
    elif int(each[0]) <= 5431:
        writer80.writerow(each)
    else:
        writer100.writerow(each)
