__author__ = 'devashishthakur'
import rpyExample
readFile = open("../dataFiles/pageRankForEachIp.csv")
writeFile = open("../dataFiles/anomalousIps","w")
ipMap = {}
for line in readFile:
    if line.split(",")[0] == "IP":
        continue

    ipMap[line.split(",")[0]] = (line.split(",")[2].rstrip()).split("##")

changedIp = {}
for el in ipMap:
    arr = [float(x) for x in ipMap[el]]
    changeValue =  rpyExample.estimate_cp_r_(arr,penalty_value=2.0)
    if len(changeValue) != 0:
        changedIp[el] = changeValue

print('Length of changed IP Map = ',len(changedIp.keys()))

# sortedValues = sorted(changedIp.items(),key=lambda x : x[1],reversed = True])

for el in changedIp:
    writeFile.write(el)
    writeFile.write("\n")
    arrval = ipMap[el]
    arrval = [float(x) for x in arrval]
    arrval = [x/min(arrval) for x in arrval]
    # print("{} = {} and {} ".format(el,changedIp[el],arrval))