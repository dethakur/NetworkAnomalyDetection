file = open("../dataFiles/a.txt")
import pickle
import networkx as nx

# dayWiseData = {}
# for line in file:
#     arr = line.split()
#     date = arr[1]
#
#     if not date in dayWiseData:
#         dayWiseData[date] = []
#
#     dayWiseData[date].append(line)

dayWiseData = pickle.load(open("../pickle/dayWiseTestData.pkl","rb"))
# print(dayWiseData)
# print(dayWiseData.keys())
# pickle.dump(dayWiseData,open("../pickle/dayWiseTestData.pkl", "wb"))
# dayVal = 1
# ipMap = {}
# for el in dayWiseData:
#     print(el)
#     for data in dayWiseData[el]:
#         arr = data.split()
#         val = (arr[7],arr[8])
#         ip1 = arr[7]
#         ip2 = arr[8]
#
#         if not ip1 in ipMap:
#             ipMap[ip1] = []
#
#         if not ip2 in ipMap:
#             ipMap[ip2] = []
#
#         ipMap[ip1].append(data)
#         ipMap[ip2].append(data)
#
# pickle.dump(ipMap,open("../pickle/ipMapTestData.pkl","wb"))
ipMapData = pickle.load(open("../pickle/ipMapTestData.pkl","rb"))
errorIp = {}
for el in ipMapData:
    values = ipMapData[el]
    for value in values:
        arr = value.split()
        if arr[-1] != "-":
            if not el in errorIp:
                errorIp[el]=True
            break


pickle.dump(errorIp,open("../pickle/flaggedIps.pkl","wb"))


    for el in edgeArr:
        graph.add_edge(el[0],el[1],weight=edgeArr[el])

    pageRank = nx.pagerank(graph)
    for el in pageRank:
        print("{} = {}".format(el,pageRank[el]))

    pickle.dump(graph,open("../pickle/graph-"+str(dayVal)+"-data.pkl", "wb"))
    dayVal += 1

    break





