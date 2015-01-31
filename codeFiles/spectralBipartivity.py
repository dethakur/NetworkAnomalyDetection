from networkx.classes.graph import Graph

__author__ = 'devashishthakur'

import networkx as nx
from networkx.algorithms import bipartite
import statistics

globalMap = {}

dayMap = {}
allNodes = {}

srcIpMap = {}
srcIpDestIpCount = {}
destIpSet = set()
# writeFile = open("../dataFiles/degree-closeness.csv","w")
writeFile = open("../dataFiles/graphIsomorphism","w")
for dayVal in range(1,16):
    readFile = open("../dataFiles/sipscan-comp-"+str(dayVal));
    edgeArr = {}

    G = nx.Graph()
    nodes = {}
    for line in readFile:
        length = len(line.split(","))
        if length != 8:
            continue

        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]

        allNodes[srcIp] = None
        nodes[srcIp] = True

        srcIpMap[srcIp] = destIp

        if not srcIp in srcIpDestIpCount:
            srcIpDestIpCount[srcIp] = {}

        srcIpDestIpCount[srcIp][destIp] = True

        destIpSet.add(destIp)

        if (srcIp,destIp) not in edgeArr:
            edgeArr[(srcIp,destIp)] = True

    G.add_edges_from(edgeArr)
    G = nx.projected_graph(G,list(nodes.keys()))
    connected_comp = nx.connected_component_subgraphs(G)
    # print(nx.number_connected_components(G))


    dayMap[dayVal] = connected_comp
    print("Done for Day ",dayVal)

anomalyGraph = {}
# writeFile.write("\n \n \n")
# writeFile.write("day,component_size,%destIpSpanned")
# writeFile.write("\n")

for day in dayMap:
    components = dayMap[day]
    comp_no = 1
    ipCountMap = {}

    writeFile.write("Data for Day ========"+str(day))
    writeFile.write("\n \n")
    for graph in components:
        nodesArr = graph.nodes()
        if len(nodesArr) < 100 :
            continue

        if not day in anomalyGraph:
            anomalyGraph[day] = []

        nodeMap = nx.degree_centrality(graph)

        sorted_nodes = sorted(nodeMap.items(),key=lambda x : x[1],reverse=True)
        # print(sorted_nodes)
        print(sorted_nodes[:5])
        for valid_node in sorted_nodes[5:]:
            graph.remove_node(valid_node[0])

        print('Nodes = ',graph.nodes())
        anomalyGraph[day].append(graph)

for day in anomalyGraph:
    for outerGraph in anomalyGraph[day]:
        for otherDays in anomalyGraph:
            if otherDays == day:
                continue

            for innerGraph in anomalyGraph[otherDays]:
                if nx.is_isomorphic(outerGraph,innerGraph):
                    print("{},{} Match is True".format(day,otherDays))
                # else:
                    # print("{},{} Match is False".format(day,otherDays))









