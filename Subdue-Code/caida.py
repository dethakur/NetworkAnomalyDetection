import pickle
import networkx as nx
import matplotlib.pyplot as plt
import math
import rpyExample
import operator
from db import DB
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import time
import graph
import randomGraph
import dimred
import collections


class Caida:
    def __init__(self):
        self.db = DB('caida2')

    def plot(self, day):
        sql = "select source, dest from raw%d " % day
        data = self.db.get_data(sql)
        G = nx.Graph()
        for tup in data:
            G.add_edge(tup[0], tup[1])
        print "plotting"
        C = nx.connected_component_subgraphs(G)
        l = []
        for c in C:
            edges = len(c.edges())
            vertices = len(c.nodes())
            l.append((edges, vertices))
        sum_edges, sum_vertices = 0, 0
        size = len(l)
        for ele in l:
            sum_edges += ele[0]
            sum_vertices += ele[1]
        print "%d, %f, %f" % (size, sum_edges / size, sum_vertices / size)


    def line_plot(self, xarray, yarray, xlabel="x", ylabel="y"):
        plt.plot(xarray, yarray)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def plotgeo(self, table):
        sql = "select lat, lng, country from %s order by source limit 1000" % table
        data = self.db.get_data(sql)
        # x = [tup[0] for tup in data]
        # y = [tup[1] for tup in data]
        # self.line_plot(x, y, "lat", "lng")

        plt.scatter()
        for (xe, ye, country) in data:
            plt.annotate(country, xy=(xe, ye), xytext=(-20, 20), textcoords='offset points', ha='right', va='bottom',
                         bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))


    def plotgeo2(self, table):
        sql = "select lat, lng, country, count(*) from %s group by country order by source" % table
        data = self.db.get_data(sql)
        x = [tup[0] for tup in data]
        y = [tup[1] for tup in data]
        size = [tup[3] for tup in data]

        countries = [tup[0] for tup in self.db.get_data("select distinct country from %s" % table)]
        colors = np.random.rand(len(countries))
        colormap = {}
        for index, c in enumerate(countries):
            colormap[c] = colors[index]

        npy = np.array(y)
        npx = np.array(x)
        plt.scatter(npx, npy, s=2, c=colors)

        # for (x, y, label, ct) in data:
        # plt.annotate(
        # label,
        # xy=(x, y), xytext=(-20, 20),
        # textcoords='offset points', ha='right', va='bottom',
        # bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        # arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))


    def plotgeo3(self, table):
        colormap = {}
        countries = [tup[0] for tup in self.db.get_data("select distinct country from %s" % table)]
        colors = np.random.rand(len(countries))
        for index, c in enumerate(countries):
            colormap[c] = colors[index]

        plots = []
        for c in countries:
            sql = "select lat, lng, country, count(*) from %s where country='%s' order by source" % (table, c)
            data = self.db.get_data(sql)
            x = [tup[0] for tup in data]
            y = [tup[1] for tup in data]
            size = [tup[3] for tup in data]
            npy = np.array(y)
            npx = np.array(x)
            c_ = colormap[c]
            print c_
            plots.append(plt.scatter(npx, npy, s=size, c=c_))

        plt.legend(tuple(plots),
                   tuple(countries),
                   scatterpoints=1,
                   loc='lower left',
                   ncol=3,
                   fontsize=8)


    def addfromgen(self, conns1, gs):
        for i in conns1:
            gs.append(i)

    def getSubCompSizeAndFreq(self, g1):
        gs = []
        connected_subcomps = nx.connected_component_subgraphs(g1)

        self.addfromgen(connected_subcomps, gs)
        print "num connected subcomps:%d " % len(gs)

        start = time.time()
        map = self.getIsomorphicGroups(gs)
        end = time.time()
        print "time taken for getting isomorphic groups:%f " % (end - start)

        print "num isomorphs:%d " % len(map)

        res = []
        for indexes in map.values():
            numnodes = len(gs[indexes[0]].nodes())
            fq = len(indexes)
            map = {"freq": fq, "nodes": numnodes, "metric": fq * numnodes}
            # print map
            res.append(map)
        return res

    def printdebug(self, gs, i):
        print "checking:%d Nodes:%d Edges:%d" % (i, len(gs[i].nodes()), len(gs[i].edges()))

    def getIsomorphicGroups(self, gs):
        i = 0
        taken = {}
        map = defaultdict(list)
        while (i < len(gs)):
            # self.printdebug(gs, i)
            if (taken.has_key(i)):
                i += 1
                continue
            j = i + 1
            while (j < len(gs)):
                # self.printdebug(gs, j)
                isim = nx.faster_could_be_isomorphic(gs[i], gs[j])
                if (isim):
                    if not (map.has_key(i)):
                        map[i].append(i)
                    map[i].append(j)
                    taken[j] = i
                j += 1
            i += 1

        self.updateNonIsomorphs(map, gs)

        return map

    def updateNonIsomorphs(self, map, gs):
        import itertools

        list2d = [ele for ele in map.values()]
        merged = list(itertools.chain(*list2d))
        for i, j in enumerate(gs):
            if not (merged.__contains__(i)):
                map[i].append(i)


    def graph_analyze(self):
        g1 = nx.Graph()
        g1.add_edge(1, 2)
        g1.add_edge(2, 3)
        g1.add_edge(3, 1122)
        g1.add_edge(3, 1)
        g1.add_edge(10, 11)

        g1.add_edge(22, 12)
        g1.add_edge(12, 43)
        g1.add_edge(43, 22)
        g1.add_edge(43, 122)
        g1.add_edge(100, 111)

        self.getSubCompSizeAndFreq(g1)


    def getGraph(self, table):
        sql = " select source, dest from %s limit 100000" % table
        print sql
        data = self.db.get_data(sql)
        print "loaded data for %s " % table
        g = nx.Graph()
        for tup in data:
            g.add_edge(tup[0], tup[1])
        print "returning"
        return g

    def graph_analyze_actual(self, table, graph):
        g = self.getGraph(table)
        print g
        res = self.getSubCompSizeAndFreq(g)
        return res

    def analysisPlot(self, table, graph=None, scalefunc=lambda x: x):
        component_metrics = self.graph_analyze_actual(table, graph)
        x = [scalefunc(map["freq"]) for map in component_metrics]
        y = [scalefunc(map["nodes"]) for map in component_metrics]

        plt.title("Day %s" % table[8:])
        plt.xlabel("Frequency")
        plt.ylabel("Size")

        npy = np.array(y)
        npx = np.array(x)
        plt.scatter(npx, npy, s=20, c=np.random.rand(len(npx)))
        dimred.lineFitWoOutliers(npx, npy, table)

    def getnpxnpy(self, component_metrics, scalefunc):
        x = [scalefunc(map["freq"]) for map in component_metrics]
        y = [math.log(map["nodes"]) for map in component_metrics]
        npy = np.array(y)
        npx = np.array(x)
        return npx, npy

    def getmetrics(self, i, scalefunc):
        component_metrics = pickle.load(open("/tmp/cm_%d" % i, 'r'))
        return self.getnpxnpy(component_metrics, scalefunc)

    def allPlot(self, color, i, npx, npy):
        plt.subplot(5, 3, i + 1)
        plt.title("Day %d" % i)
        plt.xlabel("Frequency")
        plt.ylabel("Size")
        plt.xlabel("Frequency")
        plt.ylabel("Size (nodes)")
        # plt.xlabel("Isomorphic sub-component frequency")
        # plt.ylabel("Sub-component size (nodes)")

        plt.scatter(npx, npy, s=40, c=np.array([color] * len(npx)))

    def analysisPlotAllinOne(self, scalefunc=lambda x: x):
        cm = plt.get_cmap('gist_rainbow')
        for i in range(15):
            color = cm(1. * i / 15)
            npx, npy = self.getmetrics(i, scalefunc)
            self.allPlot(color, i, npx, npy)

    def anomDetect(self, datafunc, scalefunc=lambda x: x):
        twod = []
        for i in range(15):
            npx, npy = datafunc(i)
            mtx = [[npx[j], npy[j]] for j in range(len(npx))]
            projection = dimred.mypca(mtx)
            twod.append(projection)
        sizes = [len(p) for p in twod]
        map = defaultdict(lambda: 0)
        index = 0
        while (index < min(sizes)):
            arr = []
            for p in twod:
                val = 0 if len(p) <= index else p[index]
                arr.append(val)
            anomidx = rpyExample.estimate_cp_r_(arr)
            if len(tuple(anomidx)) > 0:
                map[tuple(anomidx)[0]] += 1
            index += 1
        sortedtups = sorted(map.items(), key=operator.itemgetter(1), reverse=True)
        print "** anom is %d **" % sortedtups[0][0]


    def metricsAnalysis(self, scalefunc=lambda x: x):
        cm = plt.get_cmap('gist_rainbow')
        for i in range(15):
            color = cm(1. * i / 15)
            npx, npy = self.getmetrics(i, scalefunc)
            self.allPlot(color, i, npx, npy)


    def customGraph(self):
        nx.Graph()
        orig, anomg = randomGraph.CustomData.getUnionRandom()
        # orig = nx.bipartite_gnmk_random_graph(100, 170, 230)
        # graph.PlotGraph().colorSubcomps(orig, "neato")
        # plt.subplot(1,2,1)
        # nx.draw(orig)
        # plt.subplot(1,2,2)
        caida.analysisPlot("", orig)

    def cutomGraphAnalysis(self):
        j = 7
        for i in range(15):
            g = randomGraph.CustomData.getSaved(i, j)
            cm = self.graph_analyze_actual("", g)
            pickle.dump(cm, open("/tmp/cm_%d" % i, "w"))

    def insitunxy(self, i, j, scalefunc1):
        # g = randomGraph.CustomData.getSaved(0, j)  # todo hardcoding i
        table = "smallraw%d" % (i + 1)
        print "table is %s" % table
        # g = self.getGraph(table)
        cm = self.graph_analyze_actual(table, None)
        npx, npy = self.getnpxnpy(cm, scalefunc1)
        return npx, npy

    def getDarpaSaved(self, i, j):
        if i == j:
            return self.darpaAnom(i)
        else:
            return self.darpa(i)


    def insituCutomGraphAnalysis(self, scalefunc1=lambda x: x, anomDay=[]):
        colors = plt.get_cmap('gist_rainbow')
        slopes = []
        for i in range(15):
            # j = i if anomDay.__contains__(i) else None
            npx, npy = self.insitunxy(i, None, scalefunc1)
            color = colors(2. * i / 15)
            self.allPlot(color, i, npx, npy)
            if len(npx) > 0:
                slope = dimred.lineFitWoOutliers(npx, npy, colors(1. * (i + 1) / 15))
                slopes.append(slope)
        anomTup = rpyExample.estimate_cp_r_(slopes)
        print slopes
        print anomTup
        anomTups = tuple(anomTup)
        anomIdx = anomTups[0] if len(anomTup) > 0 else -1
        # print "anom is %d" % anomIdx
        print "print anom is"
        print anomTups
        return anomTups

    def saveXDaysTestData(self):
        for i in range(15):
            randomGraph.CustomData.getUnionRandom(i)


    def topanomtriggr(self, anom_day):
        func = lambda x: x
        # datafunc = lambda i, j: self.insitunxy(i, j, func)
        return self.insituCutomGraphAnalysis(func, anom_day)
        # self.anomDetect(datafunc)

    def withingDayAnom(self, i):
        g = randomGraph.CustomData.getSaved(i, i)
        # degs = g.degree()
        # map = collections.OrderedDict()
        # nodemap = collections.OrderedDict()
        # for k, v in degs.items():
        # if not map.__contains__(v):
        # map[v] = 0
        # nodemap[v] = []
        # map[v] += 1
        # nodemap[v].append(k)
        # # print map
        # x = np.array(map.keys())
        # y = np.array(map.values())
        # labels = dimred.kmeans(x, y)
        # anomLabel = 0 if labels.count(0) >= labels.count(1) else 1
        # freqIndexes = [o for o in len(labels) if labels[o] == anomLabel]
        # anomNodes = [node for q in freqIndexes]
        # x = degs.keys()
        # y = degs.values()
        # labels = dimred.kmeans(x, y)
        # cm = plt.get_cmap('gist_rainbow')
        # basecolors = [cm(1. * 1 / 15), cm(1. * 3 / 15)]
        # colors = [basecolors[labels[m]] for m in range(len(x))]
        # plt.scatter(x, y, s=50, c=np.array(colors))
        cm = self.graph_analyze_actual("", g)
        incr = sorted(cm.items(), key=operator.itemgetter(1))

        print cm


    def darpadata(self, sql):
        rows = self.db.get_data(sql)
        G = nx.Graph()
        for tup in rows:
            G.add_edge(tup[0], tup[1])
        return G

    def darpa(self, i):
        sql = "select src, dest from darpa%d where info is NULL or info='-' group by src, dest  limit 10000" % (i + 1)
        return self.darpadata(sql)

    def darpaAnom(self, i):
        sql = "select src, dest from darpa%d where info is not NULL or info != '-' group by src, dest  limit 10000" % (
            i + 1)
        return self.darpadata(sql)


    def darpa(self, day, ip):
        data = self.db.get_data("select src, dest from darpa%d group by src,dest" % day)
        G = nx.Graph()
        for tup in data:
            G.add_edge(tup[0], tup[1])
        comps = nx.connected_component_subgraphs(G)
        plt.title("IP: %s, Day: %d" % (ip, day))
        for c in comps:
            nodes = c.nodes()
            print "checking %d" % nodes.index(ip)
            try:
                nodes.index(ip)
                nx.draw(c)
                break
            except:
                pass



caida = Caida()
# Caida().plotgeo2("raw14")
# plt.show()

# for i in range(15):
# # plt.subplot(3, 5, 1 + i)
# caida.analysisPlot("smallraw%d" % 1, None, lambda x: math.log(x))

# Caida().analysisPlot("raw14", lambda x: math.log(x))

# Caida().condensationPlot("smallraw1")

# for i in range(15):
# plt.subplot(3, 5, 1 + i)
# Caida().condensationPlot("smallraw%d" % (i + 1), lambda x: math.log(x))


# cm = plt.get_cmap('gist_rainbow')
# colors = np.random.rand(15)
# for i in range(15):
# color = cm(1.*i/15)
# caida.analysisPlotAllinOne("smallraw%d" % (i + 1), lambda x: math.log(x), np.array([color]*15))

# caida.customGraph()
# caida.saveXDaysTestData()

# caida.cutomGraphAnalysis()
# caida.anomDetect(lambda i: caida.getmetrics(i, lambda x: x))

# caida.topanomtriggr([2])

# caida.analysisPlot("", randomGraph.CustomData.getSaved(7, -1))
# caida.withingDayAnom(12)
# caida.insituCutomGraphAnalysis()
# caida.plotgeo2("smallraw1")
# caida.darpa()

# for i in range(10):
#     plt.subplot(4,3,i)
#     print "plotting %d" %(i+1)
caida.darpa(6, "172.016.112.020")

caida.db.done()

# x = [1,2,3,4]
# y = [4,5,6,7]
# plt.plot(x,y,label="goo")
# plt.legend(loc='top')
#
plt.show()
