from mpl_toolkits.mplot3d import Axes3D
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


class NetworkAnalyser():
    def __init__(self):
        self.conn = mysql.connector.connect \
            (user='root', password='', host='127.0.0.1', database='mining')
        self.cursor = self.conn.cursor()

    def done(self):
        self.conn.close()

    def exec_and_fetch(self, query):
        self.cursor.execute("%s" % query)
        rows = self.cursor.fetchall()
        return rows

    def extract_array(self, rows, i):
        xarray = [tup[i] for tup in rows]
        return xarray

    def get_basic_x_y(self, rows):
        return self.extract_array(rows, 0), self.extract_array(rows, 1)

    def do_line_plot(self, data_method):
        x, y = data_method()
        self.line_plot(x, y)

    def line_plot(self, xarray, yarray, xlabel="x", ylabel="y"):
        plt.plot(xarray, yarray)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


    # Query methods
    def outdeg_count(self):
        x, y = self.get_day_deg_count("outdeg")
        return x, y, "Day", "Degree", "OutDegree"

    def indeg_count(self):
        x, y = self.get_day_deg_count("indeg")
        return x, y, "Day", "Degree", "InDegree"

    def get_day_deg_count(self, field):
        query = "select day, sum(%s) from day_ip_aggr group by day order by day" % (field)
        rows = self.exec_and_fetch(query)
        return self.get_basic_x_y(rows)

    def get_deg_diff_data(self):
        query = "select ip, outdeg-indeg as diff from day_ip_aggr group by ip order by diff"
        rows = self.exec_and_fetch(query)
        xarray, yarray = self.get_basic_x_y(rows)
        x = [xarray.index(i) + 1 for i in xarray]
        return x, yarray

    def max_min_outdeg_count(self):
        x, y = self.max_min_count("outdeg")
        return x, y, "Day", "Degree", "MaxOutDegree"

    def max_min_indeg_count(self):
        x, y = self.max_min_count("indeg")
        return x, y, "Day", "Degree", "MaxInDegree"

    def max_min_count(self, field):
        query = "select day, max(%s) from day_ip_aggr group by day order by day" % (field)
        print query
        rows = self.exec_and_fetch(query)
        return self.get_basic_x_y(rows)

    def protocol_count(self):
        query = "select protocol, sum(count) as tot from day_aggr group by protocol order by tot desc limit 10"
        rows = self.exec_and_fetch(query)
        xarray, yarray = self.get_basic_x_y(rows)
        prot_indexes = [xarray.index(i) for i in xarray]
        plt.plot(prot_indexes, yarray)
        plt.xlabel("Protocol")
        plt.ylabel("Count")
        plt.xticks(range(len(xarray)), xarray, size='small')

    def day_protocol_count(self):
        query = "select protocol, cast(sum(count) as unsigned) as tot, day from day_aggr group by protocol,day order by tot desc limit 10"
        rows = self.exec_and_fetch(query)
        xarray, yarray, zarray = [self.extract_array(rows, i) for i in range(0, 3)]
        prot_indexes = [xarray.index(i) for i in xarray]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(prot_indexes, yarray, zarray)
        # plt.xticks(range(len(xarray)), xarray, size='small')

    def multi_plot(self, commonx, y, y1, xlabel="None", ylabel="None", legend1="None", legend2="None", title="None"):
        plt.plot(commonx, y, label=legend1, color='b')
        plt.plot(commonx, y1, marker='o', linestyle='--', color='r', label=legend2)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()

    def do_multi_plot(self, method1, method2, title=None):
        x, y, xlabel, ylabel, legend1 = method1()
        x, y1, xlabel, ylabel, legend2 = method2()
        self.multi_plot(x, y, y1, xlabel, ylabel, legend1, legend2, title)

    def get_freq(self, field):
        sql = "select %s, count(*) c from day_ip_aggr group by outdeg order by c desc" % field
        rows = self.exec_and_fetch(sql)
        return self.get_basic_x_y(rows)

    def freq_plot_outdeg(self):
        return self.get_freq("outdeg") + ("Deg", "Freq", "Out")

    def freq_plot_indeg(self):
        return self.get_freq("indeg") + ("Deg", "Freq", "In")

    def do(self):
        # self.do_line_plot(self.max_min_indeg_count)
        # self.do_multi_plot(self.max_min_outdeg_count, self.max_min_indeg_count, "MaxDegreePlot")
        # self.protocol_count()
        # self.day_protocol_count()
        self.do_multi_plot(self.freq_plot_outdeg, self.freq_plot_indeg)
        plt.show()


analyser = NetworkAnalyser()
analyser.day_protocol_count()
analyser.do()
analyser.done()