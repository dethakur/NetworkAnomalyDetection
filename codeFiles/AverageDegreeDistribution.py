writeFile = open('../dataFiles/AverageDegreeDistributionDayWIse.csv','w')
writeFile.write("Day,Left,Average Degree,Number of nodes")
writeFile.write("\n")
for dayVal in range(1,16):
    print('Processing Day = ',dayVal)
    dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
    leftBipartiteMap = {}
    rightBipartiteMap = {}
    totalCount = 0;
    for line in dataFile:
        length = len(line.split(","))
        if length != 8:
            continue;

        totalCount += 1
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]

        if srcIp not in leftBipartiteMap:
            leftBipartiteMap[srcIp] = 0

        if destIp not in rightBipartiteMap:
            rightBipartiteMap[destIp] = 0

        leftBipartiteMap[srcIp] += 1
        rightBipartiteMap[destIp] += 1

    # print(leftBipartiteMap)
    # print(rightBipartiteMap)

    mapCount = {}

    for el in leftBipartiteMap.keys():
        avgDegree = leftBipartiteMap[el]#/totalCount
        avgDegree = round(avgDegree,8)
        # leftBipartiteMap[el] = leftBipartiteMap[el]/totalCount
        if avgDegree not in mapCount:
            mapCount[avgDegree] = 0

        mapCount[avgDegree] += 1

    print('Writing Data for Day = ',dayVal)
    print(mapCount)
    for el in mapCount:
        writeFile.write("{},{},{},{}".format(dayVal,'Left',el,mapCount[el]))
        writeFile.write("\n")

    mapCount = {}
    for el in rightBipartiteMap.keys():
        avgDegree = rightBipartiteMap[el]#/totalCount
        avgDegree = round(avgDegree,1)
        # leftBipartiteMap[el] = leftBipartiteMap[el]/totalCount
        if avgDegree not in mapCount:
            mapCount[avgDegree] = 0

        mapCount[avgDegree] += 1

    for el in mapCount:
        writeFile.write("{},{},{},{}".format(dayVal,'Left',el,mapCount[el]))
        writeFile.write("\n")

    print('Done for = ',dayVal)

    # break







