import re, sys, os, json

cwd = os.getcwd()
path = os.path.join(cwd,'WD')

content = {}

for dir, subdirs, files in os.walk(path):
    for theFile in files:

        evenOdd = int(theFile[:-4]) % 2
        wd = str(theFile[:-4])

        if evenOdd != 0:

            inPath = os.path.join(path,theFile)
            f = open(inPath).read()

            startingPoint = False

            startingPoint = re.search('ALL OCCUPATIONS LISTED ABOVE RECEIVE THE FOLLOWING BENEFITS:\n\nHEALTH & WELFARE:',f)
            endingPoint = re.search('VACATION:',f)
            if startingPoint:
                f= f[startingPoint.end():endingPoint.start()-2]

                if f != ' $4.27 per hour or $170.80 per week or $740.13 per month':
                    print(theFile)
                    print(f)
