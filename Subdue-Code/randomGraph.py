__author__ = 'devashishthakur'
import pickle
import networkx as nx
from networkx.algorithms import bipartite
from networkx import Graph
from decimal import Decimal
import rpyExample
import math
import random


class CustomGraph(nx.Graph):
    def __init__(self):
        nx.Graph.__init__(self)
        self.anomNodes = []

    def __init__(self, data=None, **attr):
        nx.Graph.__init__(self, data, **attr)
        self.anomNodes = []

    def addAnomNodes(self, nodes):
        self.anomNodes.extend(nodes)

    def degreeOfAnoms(self):
        return self.degree(self.anomNodes)


class CustomData:
    @staticmethod
    def numAnomEdges(n):
        maxcount = n * math.log(n) / 3;
        return maxcount


    @staticmethod
    def getRandomBPG(l, m, prob=0.03):
        g = nx.bipartite_random_graph(l, m, prob)
        orig = g.copy()
        print "%d %d %f" % (l, m, prob)
        # print "before: edges:%d" % len(g.edges())

        count = 0
        maxcount = CustomData.numAnomEdges(l + m)
        l, r = bipartite.sets(g)
        anom = l.pop()

        # print "adding %d anom edges" % maxcount

        for i in r:
            if not g.has_edge(anom, i) and count < maxcount:
                g.add_edge(anom, i)
                count += 1

        # print "after: edges:%d" % len(g.edges())

        return orig, g

    @staticmethod
    def minval(n, fallback=1):
        n = fallback if n == 0 else n
        return n

    @staticmethod
    def getRandomG():

        G = nx.Graph()
        H = nx.Graph()
        allAnomNodes = []
        for node in range(30):
            p = CustomData.minval(CustomData.myrand(), 0.09)
            n = int((CustomData.myrand() + CustomData.myrand()) * 10)
            n = CustomData.minval(n)
            tenp = int(p * 10 + 1)
            num_nodes = int(math.ceil(n * tenp / 3))
            recur = tenp
            g = nx.Graph()
            temp = nx.fast_gnp_random_graph(num_nodes, p)
            for j in range(recur):
                g = nx.disjoint_union(g, temp)
            dup = g.copy()
            maxAnomCount = n * math.sqrt(len(g.edges())) * p
            anomCount = 0
            nodes = g.nodes()
            if len(nodes) == 0:
                continue
            numAnomNodes = int(len(nodes) * random.randint(1, 10) / 100)
            numAnomNodes = 1 if numAnomNodes == 0 else numAnomNodes
            anomNodes = random.sample(nodes, numAnomNodes)
            random.shuffle(nodes)
            print "anom_edges:%d recur:%d nodes:%d edges:%d numAnomNodes:%d" % (
                maxAnomCount, recur, len(g.nodes()), len(g.edges()), numAnomNodes)

            for node in nodes:
                for anomNode in anomNodes:
                    if anomCount <= maxAnomCount and not g.has_edge(node, anomNode):
                        dup.add_edge(anomNode, node)
            G = nx.disjoint_union(g, G)
            H = nx.disjoint_union(dup, H)
            allAnomNodes.extend(anomNodes)
        H = CustomGraph(H)
        H.addAnomNodes(allAnomNodes)
        print (len(G.nodes()), len(G.edges()))
        print (len(H.nodes()), len(H.edges()))
        return G, H

    @staticmethod
    def getAndDump(l=100, m=100, prob=0.12):
        orig, graph = CustomData.getRandomBPG(l, m, prob)
        pickle.dump(orig, open("/tmp/orig", "w"))
        pickle.dump(graph, open("/tmp/anomgraph", "w"))
        return orig, graph

    @staticmethod
    def myrand():
        return random.random() + 0.001

    @staticmethod
    def getUnionRandom(i=0):
        orig, anom = CustomData.getRandomG()
        pickle.dump(orig, open("/tmp/orig_%d" % i, "w"))
        pickle.dump(anom, open("/tmp/anomg_%d" % i, "w"))
        return orig, anom

    @staticmethod
    def getSaved(orig, anom=None):
        file = "/tmp/anomg_%d" % anom if anom != None else "/tmp/orig_%d" % orig
        print file
        graph = pickle.load(open(file))
        if anom == orig:
            print "anom nodes are:"
            print graph.anomNodes
        return graph


    @staticmethod
    def getSavedGraph():
        return pickle.load(open("/tmp/orig", 'r')), pickle.load(open("/tmp/anomgraph", 'r'))


        # CustomData.getUnionRandom()

        # CustomData.getAndDump()


# graph = CustomGraph()
# graph.add_edge(1, 2)
# graph.addAnomNodes([2])
# # print graph.nodes()
# # print(graph.anomNodes)
#
# c = CustomGraph(graph)
# print c.nodes()