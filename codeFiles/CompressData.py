__author__ = 'devashishthakur'


validIpMap = {}

validIpFile = open("../dataFiles/validIps")
for line in validIpFile:
    validIpMap[line.split(",")[0]] = True


print(len(validIpMap.keys()))

for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-"+str(dayVal))
    writeFile = open("../dataFiles/sipscan-comp-"+str(dayVal),"w")

    ipToDegreeMap = {}
    lineArr = []

    for line in dataFile:

        length = len(line.split(","))
        srcIp = line.split(",")[1]

        if length != 8 or not(srcIp in validIpMap):
            continue;

        writeFile.write(line)


    writeFile.flush()


    print("Done for Day Val ",dayVal)






