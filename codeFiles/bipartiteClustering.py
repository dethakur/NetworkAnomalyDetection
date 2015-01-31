__author__ = 'devashishthakur'
import networkx as nx
from networkx.algorithms import bipartite

dayMap = {}
ipMap = {}

writeFile = open("../dataFiles/bipartiteClusteringDayWise.csv","w")
for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-"+str(dayVal))
    print("Parsing Day "+str(dayVal)+" data")
    dayMap[dayVal] = {}
    edgeArr = []
    graph = nx.Graph()
    for line in dataFile:
        length = len(line.split(","))
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]

        edgeArr.append((srcIp,destIp))

    graph.add_edges_from(edgeArr)
    clusterVal = bipartite.clustering(graph,mode="dot")
    print("Clustering Done for day = ",dayVal)
    for el in clusterVal:
        # if el not in ipMap:
        #     ipMap[el] = []
        #
        # ipMap[el].append(clusterVal[el])

        writeFile.write("{},{},{}".format(str(dayVal),str(el),clusterVal[el]))
        writeFile.write("\n")

    writeFile.flush()
    print("Writing Done for day = ",dayVal)

# for el in ipMap:
#     writeFile.write("{},{}".format(str(el),"##".join([str(x) for x in ipMap[el]])))
#     writeFile.write("\n")






