__author__ = 'devashishthakur'

import networkx as nx
from networkx.algorithms import bipartite

# writeFile = open("../dataFiles/nodeRedundancyDayWise","w")
dataFile = open("../dataFiles/sipscan")
validIpFile = open("../dataFiles/validIp","w")


edgeArr = []
G = nx.Graph();
duplicate = {}
lineArr = []
for line in dataFile:
    lineArr.append(line)
    length = len(line.split(","))
    if length != 8:
        continue;
    srcIp = line.split(",")[1]
    destIp = line.split(",")[length -2]
    strVal = srcIp + "-" + destIp
    if strVal not in duplicate:
        duplicate[strVal] = True
        edgeArr.append((srcIp,destIp))

print('Read all the lines atleast!!!')
G.add_edges_from(edgeArr)
print('Edges created')

# redundancyMap = bipartite.node_redundancy(G)

redundancyMap = bipartite.node_redundancy(G)

print('Redundancy calculated')

validIps = {}
for el in redundancyMap:
    if redundancyMap[el] != 0.0 and (el not in validIps):
        validIps[el] = True

for el in validIps:
    validIpFile.write(el)
    validIpFile.write("\n")

validIpFile.flush()

# print('Now doing day wise calculations ')
# for dayVal in range(1,16):
#     dataFile = open("../dataFiles/sipscan-"+str(dayVal))
#     writeFile = open("../dataFiles/sipscan-new-"+str(dayVal),"w")
#     for line in dataFile:
#         lineArr.append(line)
#         length = len(line.split(","))
#         if length != 8:
#             continue;
#         srcIp = line.split(",")[1]
#         destIp = line.split(",")[length -2]
#
#         # print(redundancyMap)
#         if srcIp in validIps or destIp in validIps:
#             writeFile.write(line);
#         # else:
#         #     writeFile2.write(line)
#
#     writeFile.flush()
#     print("Done for day = ",dayVal)
#     break
#
#
#
