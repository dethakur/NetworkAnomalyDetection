__author__ = 'devashishthakur'

import matplotlib.pyplot as plt

readFile = open("../dataFiles/bipartiteClusteringDayWise.csv")

dataMap = {}
count = 0
for line in readFile:
    day = line.split(",")[0]
    if not day in dataMap:
        if count >= 15:
            break
        count+=1
        dataMap[day] = []

    dataMap[day].append(line.split(",")[2])

count =1;
for el in dataMap:
    dayVal = el
    data = dataMap[el]
    data = [float(x) for x in data]
    uniQueMap = {}
    for el in data:
        if el not in uniQueMap:
            uniQueMap[el] = 0

        uniQueMap[el] += 1

    print('maxValue = ',max(data))
    print('minValue = ',min(data))
    xArr = []
    yArr = []

    sorted_val = sorted(uniQueMap.items(),key=lambda x : x[1],reverse=False)
    # for el in sorted_val:
    #     print(el)

    for el in uniQueMap:
        # print("{},{}".format(str(el),str(uniQueMap[el])))
        xArr.append(float(el))
        yArr.append(float(uniQueMap[el]))
    # x = data
    # y = data
    # print(len(x))
    # print("---")
    # print(len(y))
    plt.subplot(4,4,int(dayVal))
    plt.scatter(xArr,yArr)
    plt.title(str(dayVal))

    count+=1

plt.show()