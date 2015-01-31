# readFile = open("../dataFiles/ipRankFile.csv")
# writeFile = open("../dataFiles/ipRankFileFormatted-New.csv","w")
#
# mapVal = {}
# dayVal = {}
# for line in readFile:
#     day = line.split(",")[0]
#     ip = line.split(",")[1]
#     rank = line.split(",")[2]
#     if ip not in mapVal:
#         mapVal[ip] = {}
#
#     if day not in dayVal:
#         dayVal[day] = []
#
#     dayVal[day].append(float(rank))
#     mapVal[ip][day] = float(rank)
#
# # writeFile = open("../dataFiles/pageRankOutCome","w")
#
# print('Number of keys = ',len(mapVal.keys()))
#
# for el in mapVal:
#     arr = []
#
#     for dayValue in mapVal[el]:
#         sumValue = sum(dayVal[dayValue])
#         mapVal[el][dayValue] = (mapVal[el][dayValue])/sumValue
#
# for el in mapVal:
#     if len(mapVal[el].keys()) > 8:
#
#         for dayVal in mapVal[el]:
#
#             writeFile.write('{},{},{}'.format(el,dayVal,mapVal[el][dayVal]))
#             writeFile.write("\n")
#
# writeFile.flush()

# import matplotlib.pyplot as plt
# import matplotlib.lines as lines
#
# xarray=[1,2,3,4]
# yarray=[4,1,3,2]
#
# plt.plot(xarray, yarray)
# plt.xlabel("")
# plt.ylabel("")
# plt.show()
# import statistics
# dataFile = open("../dataFiles/pageRank-sipscan-compressed.csv")
# writeFile = open("../dataFiles/validIpRank-compressed.csv","w")
#
# dayMap = {}
# ipMap = {}
# count = 1
# for line in dataFile:
#     day = line.split(",")[0]
#     ipVal = line.split(",")[1]
#     rank = line.split(",")[2]
#     if ipVal not in ipMap:
#         ipMap[ipVal] = {}
#
#     ipMap[ipVal][day] = rank.rstrip()
#     if day not in dayMap:
#         dayMap[day] = []
#
#     dayMap[day].append(float(rank.rstrip()))
# # print(len(ipMap.keys()))
#
# print('Done reading 4 MB !!!')
# eachDaySumMap = {}
#
# for el in dayMap:
#    eachDaySumMap[el] = sum(dayMap[el])/len(dayMap[el])
#
# for el in ipMap:
#     arrayVal = []
#     strVal = []
#     for dayVal in ipMap[el]:
#         value = ipMap[el][dayVal]
#         strVal.append(dayVal+"##"+value)
#         arrayVal.append(float(value)/float(eachDaySumMap[dayVal]))
#
#     # arrayVal = ipMap[el]
#
#     floatArrVal = [float(a) for a in arrayVal]
#     sumVal = sum(floatArrVal)
#     # floatArrVal = [x/sumVal for x in floatArrVal]
#
#     arrayVal = [str(x) for x in floatArrVal]
#
#     stdDev = statistics.stdev(floatArrVal)
#     strVal = "@@".join(strVal)
#
#     writeFile.write("{},{},{}".format(el,str(stdDev),strVal))
#     writeFile.write("\n")
#
# writeFile.flush()
import statistics
# writeFile = open("../dataFiles/pageRankForEachIp.csv","w")
# writeFile.write("IP,StdDev,PageRank")
# writeFile.write("\n")
# readFile = open("../dataFiles/pageRank-sipscan-compressed.csv")
# ipMap = {}
# for line in readFile:
#
#     ip = line.split(",")[1]
#     value = line.split(",")[2]
#     if ip not in ipMap:
#         ipMap[ip] = []
#
#     ipMap[ip].append(value.rstrip())
#
#
# for el in ipMap:
#     stdDev = statistics.stdev([float(x) for x in ipMap[el]])
#     writeFile.write("{},{},{}".format(el,stdDev,"##".join(ipMap[el])))
#     writeFile.write("\n")
writeFile = open("../dataFiles/neighbourVsEdges.csv","w")
writeFile.write("Day,IP,Neighbours,Edges")
writeFile.write("\n")

import networkx as nx
for dayVal in range(1,16):
    readFile = open("../dataFiles/sipscan-"+str(dayVal))
    graph = nx.Graph()
    edgeArr = []
    srcIpMap = {}
    for line in readFile:
        length = len(line.split(","))
        srcIp = line.split(",")[1]
        srcIpMap[srcIp] = True
        destIp = line.split(",")[length -2]
        edgeArr.append((srcIp,destIp))

    graph.add_edges_from(edgeArr)

    pG = graph
    # pG = nx.projected_graph(graph,list(srcIpMap.keys()))

    x = nx.edges(pG)
    edgeMap = {}
    for el in x:
        left = el[0]
        right = el[1]
        if not left in edgeMap:
            edgeMap[left] = {}
        if not right in edgeMap:
            edgeMap[right] = {}

        edgeMap[left][right] = True
        edgeMap[right][left] = True


    for el in edgeMap:
        existing_edges = len(edgeMap[el].keys())
        key_val = set(edgeMap[el].keys())

        length = 0
        for node in key_val:
            connected_nodes = set(edgeMap[node])
            intersecting_nodes = connected_nodes.intersection(key_val) - set(el)
            length += len(intersecting_nodes)

        length /= 2
        number_of_neighbours = existing_edges
        edges = number_of_neighbours+length

        writeFile.write("{},{},{},{}".format(dayVal,el,number_of_neighbours,edges))

        writeFile.write("\n")

        # if length != 0:
        #     print("For Ip = {} , the original edges is = {} and will be increased by {}".format(el,existing_edges,length))

    print('Done for {}'.format(dayVal))
    writeFile.flush()