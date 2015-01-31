__author__ = 'devashishthakur'

import numpy as np
import matplotlib.pyplot as plt

# readFile =  open('../dataFiles/nodeRedundancyDayWise.csv')
readFile =  open('../dataFiles/nodeClusteringDayWise')
dayMap={}
overAllX=[]
overAllY=[]
for line in readFile:
    day = line.split(",")[0].rstrip()

    if not day.isdigit():
        continue


    x = line.split(",")[2].rstrip()
    y = line.split(",")[1].rstrip()

    if y == '0.0':
        continue

    # if y == '1.0':
    #     continue

    # if int(x) < 100:
    #     print(line)
    #     continue

    if day not in dayMap:
        dayMap[day] = {}
        dayMap[day]['x'] = []
        dayMap[day]['y'] = []
        dayMap[day]['sum'] = 0

    overAllX.append(x)
    overAllY.append(y)
    dayMap[day]['sum'] += float(x)
    dayMap[day]['x'].append(x)
    dayMap[day]['y'].append(y)

pltArr = []
count = 1;

# for el in dayMap:
#      # if count % 4 ==0
#      # pltArr.append()
#      plt.subplot(4,4,int(el))
#      xArr = []
#      # print('Original X = ',dayMap[el]['x'])
#      # print('Day Value ',dayMap[el]['sum'])
#      for arrValue in dayMap[el]['x']:
#         xArr.append(float(arrValue)/float(dayMap[el]['sum']))
#
#      # x = xArr
#      y = dayMap[el]['x']
#      # print("x=",x)
#      x = dayMap[el]['y']
#      # print("y",y)
#      plt.scatter(x,y)
#      # plt.xticks([])


plt.scatter(overAllY,overAllX)
plt.show()



