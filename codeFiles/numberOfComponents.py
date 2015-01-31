__author__ = 'devashishthakur'
import networkx as nx
from networkx.algorithms import bipartite

readFile = open("../dataFiles/sipscan-3")
validIpFile = open("../dataFiles/validIps")

srcNodes = []
for line in validIpFile:
    srcNodes.append(line.split(",")[0])


edgeMap = {}
edgeArr = []

G = nx.Graph()
validNodes = []
for line in readFile:

    length = len(line.split(","))
    srcIp = line.split(",")[1]
    destIp = line.split(",")[length -2]

    keyVal = srcIp+"-"+destIp;
    if keyVal not in edgeMap:
        edgeMap[keyVal] = True
        edgeArr.append((srcIp,destIp))
        validNodes.append(srcIp)


srcNodes = list(set(srcNodes)- (set(srcNodes) - set(validNodes)))
G.add_edges_from(edgeArr)
PG = bipartite.projected_graph(G,srcNodes)

listVal = nx.connected_components(PG)

for el in listVal:
    length = len(el)
    if length < 5:
        continue
    print(length)


# print(nx.number_connected_components(G))
# print(nx.number_connected_components(PG))









