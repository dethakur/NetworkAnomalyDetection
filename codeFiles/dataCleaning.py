__author__ = 'devashishthakur'

import networkx as nx
from networkx.algorithms import bipartite

# writeFile = open("../dataFiles/nodeRedundancyDayWise","w")
for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
    writeFile = open("../dataFiles/sipscan-redundancy-"+str(dayVal),"w")
    writeFile2 = open("../dataFiles/sipscan-redundancy-Zero-"+str(dayVal),"w")
    edgeArr = []
    G = nx.Graph();
    lineArr = []
    for line in dataFile:
        lineArr.append(line)
        length = len(line.split(","))
        if length != 8:
            continue;
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]
        edgeArr.append((srcIp,destIp))

    print('File Read , Now Creating Graph for Day val = ',dayVal)

    G.add_edges_from(edgeArr)
    print('Edges created')

    # redundancyMap = bipartite.node_redundancy(G)

    redundancyMap = bipartite.node_redundancy(G)

    validIps = {}
    for el in redundancyMap:
        if redundancyMap[el] != 0.0:
            validIps[el] = True
    # print(redundancyMap)
    print('Redundancy done for Day = ',dayVal)
    print('Now writing into the file for day = ',dayVal)
    for line in lineArr:
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]
        if srcIp in validIps or destIp in validIps:
            writeFile.write(line);
        else:
            writeFile2.write(line)

    writeFile.flush()
    writeFile2.flush()
    print("Done for day = ",dayVal)





