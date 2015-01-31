import matplotlib.pyplot as plt
from matplotlib.mlab import PCA
import pylab as pl
import numpy as np
from sklearn import cluster, datasets

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from sklearn import decomposition
from sklearn import datasets
import numpy as np
from sklearn.preprocessing import normalize
import statistics
import math

iris = datasets.load_iris()

# reduce dimension of data to 1
def mypca(data):
    global pca, npxarr, i, pts
    pca = decomposition.PCA(n_components=1)
    pca.fit(data)
    npxarr = pca.transform(data)
    # print "exp_var_ratio %f" % pca.explained_variance_ratio_
    return [i[0] for i in npxarr]


# data2 = [[1, 2],
# [5, 4]
# ]
#
# data = np.array([
# [1, 2, 3],
# [-1, -2, -3],
# [-1, -2, -3]
# ])
#
# print data * 1120
data3 = [
    [1, 2],
    [2, 4],
    [3, 6],
]


def linefit(x_range, y_range):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_range, y_range)
    formula = "%f * x + %f" % (slope, intercept)
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)


def linefit2(x, y):
    x, y = np.array(x), np.array(y)
    p = np.polyfit(x, y, 2)
    print p
    plt.plot(x, p[0] * x * x + p[1] * x + p[2])
    plt.scatter(x, y, color='r')
    plt.show()


def normalize(array):
    x = np.array(array)
    return x / np.linalg.norm(x)


    # x = [1, 2, 6, 3, 20]
    # y = [4, 5, 11, 6, 0]
    # plt.scatter(x, y)
    # graph(x, y)
    # plt.show()



    # import numpy as np
    # from scipy.optimize import curve_fit
    #
    #
    # def func(x, a, b, c):
    # return a * np.exp(-b * x) + c
    #
    #
    # xdata = np.linspace(0, 4, 50)
    # y = func(xdata, 2.5, 1.3, 0.5)
    # ydata = y + 0.2 * np.random.normal(size=len(xdata))
    # popt, pcov = curve_fit(func, xdata, ydata)


# import numpy as np
#
# K = np.random.normal(size=(2, 2))
# # print K
# data = [[1, 2, 3],
# [2, 4, 6],
# [3, 6, 9],
# ]
# eigenvalues, eigenvectors = np.linalg.eig(np.array(data))
#
# print eigenvectors


# linefit2([1, 2, 3, 77], [4, 5, 6, 2])

# x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
# z = np.polyfit(x, y, 3)
# poly1d = np.poly1d(z)
# p30 = np.poly1d(np.polyfit(x, y, 30))
#
# import matplotlib.pyplot as plt
#
# xp = np.linspace(-2, 1, 10)
# # _ = plt.plot(x, y, '.', xp, poly1d(xp), '-', xp, p30(xp), '--')
# plt.plot(xp, poly1d(xp))
# plt.ylim(-2, 2)
#
# plt.show()


from random import random
import statsmodels.api as smapi
from statsmodels.formula.api import ols
import statsmodels.graphics as smgraphics


def doregression(x, y):
    xstddev = statistics.pstdev(x)
    ystddev = statistics.pstdev(y)

    avgx = statistics.mean(x)
    tuple_list = [(x[i], y[i]) for i in range(len(x)) if math.fabs(x[i]) <= math.fabs(avgx)]


    x = [tup[0] for tup in tuple_list]
    y = [tup[1] for tup in tuple_list]
    print(ystddev)
    print(xstddev)
    print tuple_list

    print y
    print x
    regression = ols("data ~ x", data=dict(data=y, x=x)).fit()
    test = regression.outlier_test()
    outliers = ((x[i], y[i]) for i, t in enumerate(test.icol(2)) if t < 0.5)
    outlist = list(outliers)
    print 'Outliers: ', outlist
    return regression, outlist


def lineFitWoOutliers(x, y, day=-1, color='b'):
    x = [j for j in x]
    y = [k for k in y]

    regression, outlist = doregression(x, y)

    map = {}
    for i in range(len(x)):
        map["%d_%d" % (x[i], y[i])] = True
    outmap = {}
    for t in outlist:
        outmap["%d_%d" % t] = True

    for k in outmap.keys():
        if map.__contains__(k):
            del map[k]

    newx, newy = [], []
    for k in map.keys():
        split = k.split("_")
        a, b = split
        newx.append(int(a))
        newy.append(int(b))

    regression, outliers = doregression(newx, newy)
    intercept, slope = regression.params
    npxarr, npyarr = np.array(x), np.array(y)
    plt.plot(npxarr, npxarr * slope + intercept, label="Slope:%f" % slope)
    plt.legend(loc='right', prop={'size': 8})
    # plt.savefig("/Users/kaushik/ms/code/dmining/sipscanimgs/%s"%day)
    print "%f x + %f " % (slope, intercept)
    return slope

    # plt.scatter(npxarr, npyarr)


def kmeansdemo():
    iris = datasets.load_iris()
    k_means = cluster.KMeans(3)
    k_means.fit(iris.data)

    print k_means.labels_[::10]

    print iris.target[::10]


def kmeans(x, y):
    mtx = [[x[i], y[i]] for i in range(len(x))]
    k_means = cluster.KMeans(2)
    k_means.fit(mtx)
    return k_means.labels_


x = [1, 2, 6, 3, 20]
y = [4, 5, 11, 6, 0]
z = [12, 5, 1, 6, 0]

# print kmeans(x, y)
#
# lineFitWoOutliers(x, y)
# plt.show()

