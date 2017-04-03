import os, csv, sys, re

cwd = os.getcwd()
path = os.path.join(cwd,'WD')

csvFile = open('Dropped-Counties.csv', 'r')
csvData = csv.reader(csvFile)

csvPrintFile = open('state-county-wd2.csv', 'a')
csvWriter = csv.writer(csvPrintFile)


data = []

for each in csvData:

    county = each[0]
    county = county.lower()
    state = each[1].lower()
    for dir, subdirs, files in os.walk(path):
        for theFile in files:

            inPath = os.path.join(path,theFile)
            f = open(inPath).read().lower()

            if re.search(state, f):
                if re.search(county, f):

                    array = [state.capitalize(),county.capitalize(),theFile[:-4]]
                    print(array)
                    data.append(array)
                    csvWriter.writerow(array)
                    break
                    break


csvPrintFile.close()
csvFile.close()
