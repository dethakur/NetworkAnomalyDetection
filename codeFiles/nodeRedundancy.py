__author__ = 'devashishthakur'

import networkx as nx
from networkx.algorithms import bipartite

# writeFile = open("../dataFiles/nodeRedundancyDayWise","w")
writeFile = open("../dataFiles/nodeClusteringDayWise","w")

writeFile.write("Day,Redundancy,Number")
writeFile.write("\n")
for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
    edgeArr = []
    G = nx.Graph();
    for line in dataFile:
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

    redundancyMap = bipartite.clustering(G)
    # print(redundancyMap)

    print('Redundancy done for Day = ',dayVal)

    valueMap = {}
    for el in redundancyMap:
        value = redundancyMap[el]

        if value not in valueMap:
            valueMap[value] = 0

        valueMap[value] += 1

    for el in valueMap:
        writeFile.write("{},{},{}".format(dayVal,el,valueMap[el]))
        writeFile.write("\n")

    print("Done for day = ",dayVal)



