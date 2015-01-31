__author__ = 'devashishthakur'
import networkx as nx
import rpyExample

def get_page_rank(graph_el):
    print('Calculating the page rank')
    return nx.pagerank(graph_el)

def find_number_of_arrays_with_change(ipRankArr):
    print('Inside find_number_of_arrays_with_change')
    count = 0
    for el in ipRankArr:
        arr = ipRankArr[el]
        arr = arr[-2:]
        arr = [float(x) for x in arr]

        changeValue =  rpyExample.estimate_cp_r_(arr)
        if len(changeValue) != 0:
            # print('Change observed for ip')
            count += 1

    return count


stdDevMap = {}
pageRankMapFile = open("../dataFiles/pageRankForEachIp.csv")
for line in pageRankMapFile:
    stdDevMap[line.split(",")[0].rstrip()] = str(line.split(",")[1].rstrip())

anomalousIpMap = open("../dataFiles/anomalousIps")
ipMap = {}
for line in anomalousIpMap:
    ip = line.split(",")[0].rstrip()
    ipMap[ip] = stdDevMap[ip]


sorted_val = sorted(ipMap.items(),key = lambda x : float(x[1]), reverse=True)
writeFile = open("../dataFiles/dayWiseAnomaly","w")
for dayVal in range(1,16):
    edgeArr = []
    ipRankArrMap = {}
    daywiseFile = open("../dataFiles/sipscan-"+str(dayVal))
    for line in daywiseFile:
        length = len(line.split(","))
        srcIp = line.split(",")[1]
        destIp = line.split(",")[length -2]
        edgeArr.append((srcIp,destIp))
        ipRankArrMap[srcIp] = []


    graph = nx.Graph()
    graph.add_edges_from(edgeArr)
    graph = nx.projected_graph(graph,list(ipRankArrMap.keys()))

    pageRank = get_page_rank(graph)
    for el in pageRank:
        ipRankArrMap[el].append(pageRank[el])

    buggyIps = []

    while len(sorted_val) != 0:

        ip_to_be_removed = sorted_val[0][0]
        print('Removing ',ip_to_be_removed)
        if not ip_to_be_removed in ipRankArrMap:
            print('This is not present here = ',ip_to_be_removed)
            sorted_val.remove(sorted_val[0])
            continue

        sorted_val.remove(sorted_val[0])
        buggyIps.append(ip_to_be_removed)
        graph.remove_node(ip_to_be_removed)
        del ipRankArrMap[ip_to_be_removed]

        pageRank = get_page_rank(graph)
        for el in pageRank:
            ipRankArrMap[el].append(pageRank[el])

        count = find_number_of_arrays_with_change(ipRankArrMap)
        print('Number of ips that show change = ',count)
        if count == 0 :
            print('Breaking from the loop')
            break


    print('Buggy Ips on day Val ',dayVal)

    for i in buggyIps:
        writeFile.write("{},{}".format(dayVal,"##".join(buggyIps)))
        writeFile.write("\n")
        print(buggyIps)




