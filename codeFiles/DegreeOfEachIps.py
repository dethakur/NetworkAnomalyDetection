# __author__ = 'devashishthakur'
# import statistics
#
# readFile = open("../dataFiles/validIps")
# writeFile = open("../dataFiles/ipwiseDegreeDistribution.csv","w")
#
# ipMap = {}
# for el in readFile:
#     ipMap[el.split(",")[0]] = True
#
# dayMap = {}
# ipDetails = {}
# for dayVal in range(1,16):
#     dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
#     print("Parsing Day "+str(dayVal)+" data")
#     dayMap[dayVal] = {}
#     for line in dataFile:
#         length = len(line.split(","))
#         srcIp = line.split(",")[1]
#         destIp = line.split(",")[length -2]
#
#         if length != 8 or not(srcIp in ipMap):
#             continue
#
#         if srcIp not in dayMap[dayVal]:
#             dayMap[dayVal][srcIp] = 0
#
#         dayMap[dayVal][srcIp] += 1
#
#
# for dayVal in dayMap:
#     for ip in dayMap[dayVal]:
#
#         if ip not in ipDetails:
#             ipDetails[ip] = {}
#
#         ipDetails[ip][dayVal] = dayMap[dayVal][ip]
#
#
# for el in ipDetails:
#     ip = el
#     arrayVal = []
#     strVal = []
#     for value in ipDetails[el]:
#         strVal.append(str(value)+"##"+str(ipDetails[el][value]))
#         arrayVal.append(float((ipDetails[el][value])))
#
#     stdDev = statistics.stdev(arrayVal)
#     strVal = "@@".join(strVal)
#
#
#     writeFile.write("{},{},{}".format(ip,stdDev,strVal))
#     writeFile.write("\n")
#
# writeFile.flush()
#
#
#
#
#
#


__author__ = 'devashishthakur'
import statistics

readFile = open("../dataFiles/validIps")
writeFile = open("../dataFiles/ipwiseUniqueDegreeDistribution.csv","w")

ipMap = {}
for el in readFile:
    ipMap[el.split(",")[0]] = True

dayMap = {}
ipDetails = {}

for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
    print("Parsing Day "+str(dayVal)+" data")
    dayMap[dayVal] = {}
    uniqueIpMap = {}
    for line in dataFile:
        length = len(line.split(","))
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]

        if length != 8 or not(srcIp in ipMap) or (srcIp+"-"+destIp in uniqueIpMap):
            continue

        if srcIp not in dayMap[dayVal]:
            dayMap[dayVal][srcIp] = 0

        uniqueIpMap[srcIp+"-"+destIp] = True
        dayMap[dayVal][srcIp] += 1


for dayVal in dayMap:
    for ip in dayMap[dayVal]:

        if ip not in ipDetails:
            ipDetails[ip] = {}

        ipDetails[ip][dayVal] = dayMap[dayVal][ip]


for el in ipDetails:
    ip = el
    arrayVal = []
    strVal = []
    for value in ipDetails[el]:
        strVal.append(str(value)+"##"+str(ipDetails[el][value]))
        arrayVal.append(float((ipDetails[el][value])))

    stdDev = statistics.stdev(arrayVal)
    strVal = "@@".join(strVal)


    writeFile.write("{},{},{}".format(ip,stdDev,strVal))
    writeFile.write("\n")

writeFile.flush()






