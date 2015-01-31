import networkx as nx
import matplotlib.pyplot as plt
import random
from db import DB

import sys
sys.path.append("/opt/local/bin/dot")



class PlotGraph:
    def __init__(self, d=DB()):
        self.db = d

    def colorSubcomps(self, G, prog="neato", layout=None):
        C = nx.connected_component_subgraphs(G)
        pos = nx.graphviz_layout(G, prog=prog) if layout == None else layout

        for g in C:
            c = [random.random()] * nx.number_of_nodes(g)  # random color...
            nx.draw(g, pos, node_size=40, node_color=c, vmin=0.0, vmax=1.0, with_labels=False)

    def addEdges(self, G, data_method, *args):
        rows = data_method() if len(args) == 0 else data_method(*args)
        print "got rows %s " % len(rows)
        for tup in rows:
            G.add_edge(tup[0], tup[1])


    def allNodes(self):
        return self.db.get_data("select source, dest from day_aggr where dest not like 'Broadcast'")


    def forANode(self):
        return self.db.get_data(
            "select source, dest from day_aggr where dest not like 'Broadcast' and source='10.51.16.43' and protocol like 'TCP' ")

    def dayWiseAllNodes(self, day):
        return self.db.get_data(
            "select source, dest from day_aggr where dest not like 'Broadcast' and day=%s" % day)

    def dayWiseForANode(self, day, ip):
        sql = "select source, dest from day_aggr where dest not like 'Broadcast' and day=%s and source='%s' group by source, dest" % (
        day, ip)
        print sql
        return self.db.get_data(sql)

    def dayWiseForANodeDistintTimes(self, day, ip):
        sql = "select source, time from distinct_source_time where day=%s and source='%s' " % (day, ip)
        print sql
        return self.db.get_data(sql)

    def makeGraph(self, data_method):
        G = nx.Graph()
        self.addEdges(G, data_method)
        self.colorSubcomps(G)
        plt.show()


    def makeGraphDayWise(self, data_method, *args):
        for day in range(0, 9):
            G = nx.Graph()
            plt.subplot(331 + day)
            plt.title("Day %s" % (day + 1))
            self.addEdges(G, data_method, day, *args)
            self.colorSubcomps(G)
        # plt.savefig("/Users/kaushik/Desktop/anomaly-%s.png" % args[0])
        plt.show()

    def getCaida(self):
        sql = "select source, dest from der "
        return self.db.get_data(sql)




# graph = PlotGraph(DB("mining"))

# graph.makeGraph(graph.allNodes)
# graph.makeGraphDayWise(graph.dayWiseAllNodes)
# graph.makeGraphDayWise(graph.dayWiseForANode, "10.51.16.1")

# l = ["10.51.16.41"]
# for i in l:
# graph.makeGraphDayWise(graph.dayWiseForANode, i)


# l = ["10.51.16.35"]
# for i in l:
#     graph.makeGraphDayWise(graph.dayWiseForANodeDistintTimes, i)


# graph.makeGraph(graph.getCaida)
