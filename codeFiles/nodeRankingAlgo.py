from ipaddress import ip_address
import networkx as nx
from networkx.algorithms import bipartite
import statistics

dayMap = {}
glocalCoeffChangeMap = {}

for dayVal in range(1,16):
    dataFile = open("../dataFiles/sipscan-comp-"+str(dayVal))
    # dataFile = open("../dataFiles/sipscan")
    uniqueValMap = {}
    ipMap = {}
    edgeArr = []
    graphArr = []
    coefficientMap = {}
    G = nx.Graph()
    destIpSet = set()
    sourceIpSet = set()

    print("Parsing Day "+str(dayVal)+" data")

    for line in dataFile:
        length = len(line.split(","))
        if length != 8:
            continue;
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]

        if srcIp not in ipMap:
            ipMap[srcIp] = set()

        # sourceIpSet.add(srcIp)
        # destIpSet.add(destIp)
        #
        # ipMap[srcIp].add(destIp)
        edgeArr.append((srcIp,destIp))


    # for key in ipMap.keys():
    #     if(len(ipMap[key]) > 1):
    #         print("{},{}".format(key,len(ipMap[key])))

    G.add_edges_from(edgeArr)

    print('xxx')

    arr = bipartite.clustering(G)
    for node in arr.keys():
        coefficient = arr[node]
        if coefficient not in coefficientMap:
            coefficientMap[coefficient] = []

        coefficientMap[coefficient].append(node)

    print('Clustering done for day = '+str(dayVal))

    for el in coefficientMap:
        if el not in glocalCoeffChangeMap:
            glocalCoeffChangeMap[el] = []

        glocalCoeffChangeMap[el].append(len(coefficientMap[el]))



    dayMap[dayVal] = coefficientMap

    # break


writeFile = open("../dataFiles/GlobalCoeffCount.csv","w")
writeFile.write("Coefficient, Count, SDev")
writeFile.write("\n")
for el in glocalCoeffChangeMap:
    arrval = glocalCoeffChangeMap[el]
    dev = 0
    if len(arrval) > 2 :
        dev = statistics.stdev(arrval)

    strVal = ""
    strVal += str(el)+","
    strVal += ",".join(str(x) for x in arrval)+","
    strVal += str(dev)
    writeFile.write(strVal)
    writeFile.write("\n")





