__author__ = 'devashishthakur'

import numpy as np
import matplotlib.pyplot as plt
formualeFile = open("../dataFiles/NeighbourVsEdgesLinearRegressionFormuale")

formula = None


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()

for line in formualeFile:
    formula = line.split(",")[1]
    graph(formula, range(1,10))
