import numpy as np
import matplotlib.pyplot as plt
import sys
# readFile = open('../dataFiles/neighbourVsEdges.csv')
# validIpFile = open("../dataFiles/anomalousIps")
# formualeFile = open("../dataFiles/NeighbourVsEdgesLinearRegressionFormuale")
#
# formulae = []
#
# def graph(formula, x_range):
#
#     x_range = [float(x) for x in x_range]
#     x = np.array(x_range)
#     y = eval(formula)
#     plt.plot(x, y)
#
# for line in formualeFile:
#     formulae.append(line.split(",")[1])
#
# ipMap = {}
#
#
# InvalidIpMap = {}
# # for i in validIpFile:
# #     InvalidIpMap[i.rstrip()] = True
#
# dayMap={}
# dayVal = None
#
# if len(sys.argv) > 1:
#     dayVal = sys.argv[1]
#
# for line in readFile:
#
#     day = line.split(",")[0].rstrip()
#
#
#     if not day.isdigit():
#         continue
#     if dayVal is None or day == dayVal:
#         ip = line.split(",")[1]
#
#         # if ip in InvalidIpMap:
#         #     # print("Skipping ip = ",ip)
#         #     continue
#
#         x = line.split(",")[2].rstrip()
#         y = line.split(",")[3].rstrip()
#
#         if day not in dayMap:
#             dayMap[day] = {}
#             dayMap[day]['x'] = []
#             dayMap[day]['y'] = []
#
#         dayMap[day]['x'].append(x)
#         dayMap[day]['y'].append(y)
#
# # print(dayMap.keys())
# pltArr = []
# count = 1;
# for el in dayMap:
#      x = dayMap[el]['x']
#      print(formulae[int(el)])
#      # graph(formulae[int(el)], x)
#      y = dayMap[el]['y']
#
#
#      plt.scatter(x,y)
#      # plt.xticks([])
#
#
#
#
#
#
#
# # N = 50
# # x = np.random.rand(N)
# # print(x)
# # y = np.random.rand(N)
# # # colors = np.random.rand(N)
# # area = np.pi * (2 * np.random.rand(N))**2 # 0 to 15 point radiuses
# # plt.subplot(3,5,1)
# # plt.scatter(x, y, s=area, alpha=0.5)
# # plt.subplot(3,5,2)
# # plt.scatter(x, y, s=area, alpha=0.5)
# plt.show()
# a = "0.025992330541501425##0.05076946725216723##0.06746031746031746##0.04606614575654823##0.06101108627424416##0.008771929824561403##0.03840155945419103##0.04607445551359114##0.05253409490697627##0.03383774930090912"
# a = "0.00023570233503108012, 0.0008902283196626929, 9.899616027346587e-05, 0.0002535648512186517, 0.004245700307293318, 0.022427240909040254, 0.0002202865189890292, 9.799650831864026e-05, 0.0005932130628834928, 0.0012648204850310293, 8.084807332334914e-05"
# a="0.00834830736570676, 0.004064764659607802, 0.017783892683090975, 0.006639999476086534, 0.026098552805035275, 0.13742109432184738, 0.004203571377080548, 0.0027128106535724253, 0.0030089587828604856, 0.005758775402142828, 0.002560246490187944"
# a="0.011828194362022223, 0.0021444970881565276, 0.021866718053075274, 0.0085538028741265, 0.05186212807244943, 0.2741297692440578, 0.008523494168227154, 0.006620201412032399, 0.0015130597797226213, 0.003359919261788238, 0.004131334376955171"
# a="0.010670414689494357, 0.009427808283579683, 0.0006258328876341498, 0.01621228938592329, 0.04937791347914506, 0.009938845022252035, 0.016240269843614135, 0.02158593646635193, 0.01430736724218269"
# a="0.000536160173154799, 0.0002762027751214174, 4.010561511607189e-05, 0.00025787036534457214, 0.020847889434433678, 0.0015895580070470609, 0.00014305830769981943, 0.0006576862543653959, 0.00032701648552834676, 0.00010656213647854476"
# a="0.00023720073982075982, 0.00022781257537317386, 1.947560132064381e-05, 0.00017782403015697618, 9.054577258907545e-05, 0.0001351910967163518, 0.0001997006563268435, 6.261391982664379e-05"
a="0.00021257286455837371, 0.0007797592121300826, 0.00039064166968974675, 0.00017963704515560984, 8.561384509410251e-05, 0.00013564844732262793, 0.00020830897666638572, 7.141207638886653e-05"
yarr = a.split(",")
xarr = range(len(yarr))
plt.plot(xarr,yarr)
plt.show()
