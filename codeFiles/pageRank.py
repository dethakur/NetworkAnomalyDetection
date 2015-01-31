import networkx as nx
from networkx.algorithms import bipartite
import statistics


rankMap = {}
validIpFile = open("../dataFiles/validIpRank.csv")
validIpMap = {}

for line in validIpFile:
    validIpMap[line.split(",")[0]] = True

writeFile = open("../dataFiles/pageRank-sipscan-compressed.csv","w")
for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
    print("Parsing Day "+str(dayVal)+" data")
    G = nx.Graph()
    edgeArr = []
    validEdgeMap = {}
    for line in dataFile:
        length = len(line.split(","))
        if length != 8:
            continue

        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]
        edgeArr.append((srcIp,destIp))

        if srcIp in validIpMap and not(srcIp in validEdgeMap):
            validEdgeMap[srcIp] = True

    G.add_edges_from(edgeArr)
    PG = nx.projected_graph(G,list(validEdgeMap.keys()))
    mapVal = nx.pagerank(PG)

    print(len(mapVal.keys()))
    for el in mapVal:
        writeFile.write("{},{},{}".format(dayVal,el,mapVal[el]))
        writeFile.write("\n")

    writeFile.flush()
    print("Done with dayVal =",dayVal)


# for el in rankMap:
#     ip = rankMap[el]
#     strVal = ""
#     for dayVal in rankMap[el].keys():
#         strVal += dayVal+"-"+rankMap[el][dayVal]
#
#     writeFile.write("{},{}".format(ip,strVal))
#     writeFile.write("\n")


