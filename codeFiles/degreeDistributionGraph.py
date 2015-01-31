import numpy as np
import matplotlib.pyplot as plt

readFile = open('../dataFiles/degreeDistributionDayWise.csv')

dayMap={}
for line in readFile:
    day = line.split(",")[0].rstrip()

    if not day.isdigit():
        continue
    x = line.split(",")[1].rstrip()
    y = line.split(",")[2].rstrip()

    if day not in dayMap:
        dayMap[day] = {}
        dayMap[day]['x'] = []
        dayMap[day]['y'] = []

    dayMap[day]['x'].append(x)
    dayMap[day]['y'].append(y)

print(dayMap.keys())
pltArr = []
count = 1;
for el in dayMap:
     # if count % 4 ==0
     # pltArr.append()
     plt.subplot(4,4,int(el))

     print('Plotting Day = ',el)
     print("X value = ",dayMap[el]['x'])
     print("Y value = ",dayMap[el]['y'])

     x = dayMap[el]['x']
     y = dayMap[el]['y']
     plt.scatter(x,y)
     # plt.xticks([])







# N = 50
# x = np.random.rand(N)
# print(x)
# y = np.random.rand(N)
# # colors = np.random.rand(N)
# area = np.pi * (2 * np.random.rand(N))**2 # 0 to 15 point radiuses
# plt.subplot(3,5,1)
# plt.scatter(x, y, s=area, alpha=0.5)
# plt.subplot(3,5,2)
# plt.scatter(x, y, s=area, alpha=0.5)
plt.show()
