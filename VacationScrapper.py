import os, re, csv

csvFile = open('VacationData.csv','w')
csvWriter = csv.writer(csvFile)


CWD = os.getcwd()
path = os.path.join(CWD,'WD')

StartString = ['Name','First Amount','First Cut','Second Amount','Second Cut','Third Amount','Third Cut']
csvWriter.writerow(StartString)

for dir,subdirs,files in os.walk(path):

    for each in files:
        name = each[:4]

        innerPath = os.path.join(path,each)
        innerFile = open(innerPath, 'r+').read()

        reGex = r"VACATION: (.+?) weeks paid vacation after (.+?) year of service"
        reGex2 = r", (.+?) weeks after (.+?) years, and (.+?) weeks after (.+?) years."
        match = re.finditer(reGex, innerFile)
        match2 = re.finditer(reGex2, innerFile)
        for item in match:
            firstAmt = item.group(1)
            firstCut = item.group(2)
        for thing in match2:
            secondAmt = thing.group(1)
            secondCut = thing.group(2)
            thirdAmt = thing.group(3)
            thirdCut = thing.group(4)
            VACinfo = [name,firstAmt,firstCut,secondAmt,secondCut,thirdAmt,thirdCut]
            csvWriter.writerow(VACinfo)
