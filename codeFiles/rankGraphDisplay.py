import matplotlib.pyplot as plt
import matplotlib.lines as lines
import math


stdDevMap = {}
pageRankMapFile = open("../dataFiles/pageRankForEachIp.csv")
dataMap = {}
for line in pageRankMapFile:
    stdDevMap[line.split(",")[0].rstrip()] = str(line.split(",")[1].rstrip())
    dataMap[line.split(",")[0].rstrip()] = line.rstrip()

anomalousIpMap = {}
anomalousIpFile = open("../dataFiles/anomalousIps")
for line in anomalousIpFile:
    ip = line.split(",")[0].rstrip()
    anomalousIpMap[ip] = stdDevMap[ip]

sorted_asc_ip = sorted(anomalousIpMap.items(),key=lambda x : x[1],reverse=True)
sorted_desc_ip = sorted(anomalousIpMap.items(),key=lambda x : x[1],reverse=False)



count = 0
invalidIpArrLength = 0
validIpArrLength = 4

inValidIpArr = [x[0] for x in sorted_asc_ip[0:invalidIpArrLength]]
validIpArr = [x[0] for x in sorted_desc_ip[:validIpArrLength]]

# print(inValidIpArr)
# print("---")
# print(validIpArr)
validIpRankArr = []
inValidIpRankArr = []
min_value = 10;
len1 = 100
len2 = 100
for i in range(0,max(len(validIpArr),len(inValidIpArr))):
    print("i=",i)

    if i < len(validIpArr):
        ip = validIpArr[i]
        print('Valid Ip = ',ip)
        print("Valid",dataMap[ip])
        validIpRankArr.append(dataMap[ip].split(",")[2].rstrip().split("##"))
        len1 = len(dataMap[ip].split(",")[2].split("##"))


    if i < len(inValidIpArr):
        ip = inValidIpArr[i]
        print('Invalid Ip = ',ip)
        # print("InValid = ",dataMap[ip].split(",")[2].rstrip().split("##"))
        inValidIpRankArr.append(dataMap[ip].split(",")[2].rstrip().split("##"))
        len2 = len(dataMap[ip].split(",")[2].split("##"))

    min_value = min(min_value,len1,len2)


for i in range(0,max(len(validIpArr),len(inValidIpArr))):
    xaxis = range(min_value)

    axes = plt.gca()
    axes.set_ylim([0,.04])


    if i < len(validIpRankArr):
        yaxis1 = validIpRankArr[i][:min_value]
        plt.plot(xaxis,yaxis1)

    if i < len(inValidIpRankArr):
        yaxis2 = inValidIpRankArr[i][:min_value]
        plt.plot(xaxis,yaxis2)



plt.show()
