__author__ = 'devashishthakur'
import networkx as nx
from networkx.algorithms import bipartite
from networkx import  Graph
import random
from decimal import Decimal
import statistics
import json
import rpyExample

from networkx.readwrite import json_graph


pageRankNodeMap = {}
random_bipartite_graph = Graph()
bipartite_size = 1000
random_bipartite_graph = nx.bipartite_random_graph(bipartite_size,bipartite_size,.33)
corrupted_node = {}

x, y = bipartite.sets(random_bipartite_graph)

# number_of_fake_nodes = 5
min_value_x = min(x)
max_value = max(y)
min_value = min(y)

count = 1

degreeMap = nx.degree(random_bipartite_graph)
sortedval = sorted(degreeMap.items(),key = lambda x : x[1],reverse=True)

for val in range(10):

    if val == 5:
        for node_value in range(min_value_x+10):
            node = random_bipartite_graph.nodes()[node_value]

            if not node_value in corrupted_node:
                corrupted_node[node_value] = {}

            corrupted_node[node_value]['old'] = degreeMap[node_value]
            compare_val = min_value + 0.9*(max_value - min_value)
            for node_val in range(min_value,int(compare_val)):
                edgeArr = random_bipartite_graph.edges()
                if not (node,node_val) in edgeArr:
                    random_bipartite_graph.add_edge(node,node_val)

    pageRankMap = nx.pagerank(random_bipartite_graph)
    for i in pageRankMap:
        if i not in pageRankNodeMap:
            pageRankNodeMap[i] = []

        x = Decimal(pageRankMap[i]).quantize(Decimal('0.000000001'))
        pageRankNodeMap[i].append(float(x))


degreeMap = nx.degree(random_bipartite_graph)

for el in corrupted_node:
    corrupted_node[el]['new'] = degreeMap[el]

for el in corrupted_node:
    print('IP = {} , Old = {} and new = {}'.format(el,corrupted_node[el]['old'],corrupted_node[el]['new']))


for el in pageRankNodeMap:
    arr = pageRankNodeMap[el]
    mean_val = sum(arr)
    val = rpyExample.estimate_cp_r_(arr);
    if len(val) != 0:
        print(el)


def graph_description(network_graph):
    degreeMap = nx.degree(network_graph)
    pageRank = nx.pagerank(network_graph)









