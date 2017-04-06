import os, re, csv

csvFile = open('VacationData.csv','w')
csvWriter = csv.writer(csvFile)


CWD = os.getcwd()
path = os.path.join(CWD,'WD')

StartString = ['WD','First Amount','First Cut','Second Amount','Second Cut','Third Amount','Third Cut']
csvWriter.writerow(StartString)

for dir,subdirs,files in os.walk(path):

    for each in files:
        name = each[:4]

        innerPath = os.path.join(path,each)
        innerFile = open(innerPath, 'r+').read()

        startingPoint = False

        startingPoint = re.search('ALL OCCUPATIONS LISTED ABOVE RECEIVE THE FOLLOWING BENEFITS:\n\nHEALTH & WELFARE:',innerFile)
        endingPoint = re.search('HOLIDAYS:',innerFile)

        if startingPoint:
            f = innerFile[startingPoint.end():endingPoint.start()-2]

            reGex = r"VACATION: (.+?) weeks paid vacation after (.+?) year"
            reGex2 = r" (\d) weeks after (\d\d?) years, and (\d).+?after (\d\d?) years\."
            match = re.finditer(reGex, f)
            match2 = re.finditer(reGex2, f)
            for item in match:
                firstAmt = 5* int(item.group(1))
                firstCut = item.group(2)
            for thing in match2:
                secondAmt = 5* int(thing.group(1))
                secondCut = thing.group(2)
                thirdAmt = 5* int(thing.group(3))
                thirdCut = thing.group(4)

            VACinfo = [name,firstAmt,firstCut,secondAmt,secondCut,thirdAmt,thirdCut]
            csvWriter.writerow(VACinfo)
