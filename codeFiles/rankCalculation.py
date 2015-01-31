__author__ = 'devashishthakur'

readFile = open("../dataFiles/ipRankFile.csv")

dayMap = {}
ipMap = {}
for line in readFile:
    day = line.split(",")[0]
    ip = line.split(",")[1]
    rank = line.split(",")[2]

    if day not in dayMap:
        dayMap[day] = []

    if ip not in ipMap:
        ipMap[ip] = []




