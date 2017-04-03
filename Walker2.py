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
            tablestart = re.search("FOOTNOTE               RATE", f).end()
            try:
                tableend = [m.start() for m in re.finditer(r"____________________________________________________________________________________",f)][2]
            except IndexError:
                tableend = [m.start() for m in re.finditer(r"____________________________________________________________________________________",f)][1]
            innerData = f[tablestart+1:tableend-10]
            innerData = innerData.split('\n')
            for i, lord in enumerate(innerData):
                innerData[i] = innerData[i].split(' ')
                replaceList = []

                for j, subEach in enumerate(innerData[i]):
                    if len(subEach) > 0:
                        replaceList.append(subEach.replace('\n','').replace('\r',''))

                if replaceList[0].endswith('000'):
                    setIC = replaceList[0]
                    nameMaker = len(replaceList)
                    OuterName = ' '.join(replaceList[2:])
                    tableName = setIC + ' - ' + OuterName
                else:
                    subCode = replaceList[0]
                    nameMaker = len(replaceList)
                    OuterName = ' '.join(replaceList[2:-1])
                    tableCode = str(subCode) + ' - ' + OuterName

                    if replaceList[nameMaker-1].isalpha():
                        wage = float(0.00)
                        OuterName += ')'
                    else:
                        try:
                            wage = float(replaceList[nameMaker-1])
                        except ValueError:
                            wage = float(0.00)

                    print(wd)

                    if wd in content.keys():
                        if tableName in content[wd].keys():
                            content[wd][tableName][tableCode] = {'Position Code': subCode, 'Position': OuterName, 'Wage': wage}
                        else:
                            content[wd][tableName] = {}
                            content[wd][tableName][tableCode] = {'Position Code': subCode, 'Position': OuterName, 'Wage': wage}
                    else:
                        content[wd] = {}
                        content[wd][tableName] = {}
                        content[wd][tableName][tableCode] = {'Position Code': subCode, 'Position': OuterName, 'Wage': wage}
with open('Gcontent.txt', 'w') as d:
    json.dump(content, d)
