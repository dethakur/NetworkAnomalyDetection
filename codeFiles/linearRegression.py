from scipy import stats
import numpy as np
import statistics
#
# x = np.random.random(10)
# y = np.random.random(10)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# x = 2
# y = 2
# s = slope*x + intercept
# print(s)

readFile = open("../dataFiles/neighbourVsEdges.csv")
dayMapData = {}
ipMap = {}
count = 1
for line in readFile:
    dayVal = line.split(",")[0]

    if not dayVal.isdigit():
        continue

    dayVal = int(dayVal)

    ip = line.split(",")[1]

    x = line.split(",")[2].rstrip()
    y = line.split(",")[3].rstrip()



    if not dayVal  in dayMapData:
        # if count >4:
        #     break

        count+=1
        print('Creating key for day = ',dayVal)
        dayMapData[dayVal] = {}
        dayMapData[dayVal]['x'] = []
        dayMapData[dayVal]['y'] = []
        dayMapData[dayVal]['ip'] = {}

    if not ip in dayMapData[dayVal]['ip']:
        dayMapData[dayVal]['ip'][ip] = {}



    dayMapData[dayVal]['x'].append(x)
    dayMapData[dayVal]['y'].append(y)
    dayMapData[dayVal]['ip'][ip]['x'] = x
    dayMapData[dayVal]['ip'][ip]['y'] = y



regressionLineMap = {}
writeFile = open("../dataFiles/NeighbourVsEdgesLinearRegression","w")
formualeFile = open("../dataFiles/NeighbourVsEdgesLinearRegressionFormuale","w")
for dayVal in sorted(dayMapData.keys()):
    xArr = dayMapData[dayVal]['x']
    yArr = dayMapData[dayVal]['y']

    xArr = [float(x) for x in xArr]
    yArr = [float(x) for x in yArr]

    slope, intercept, r_value, p_value, std_err = stats.linregress(xArr,yArr)
    formulae = str(slope)+"*x " +str(intercept)
    print(formulae)
    formualeFile.write("{},{}".format(dayVal,formulae))
    formualeFile.write("\n")

    for el in dayMapData[dayVal]['ip']:
        ipEl = dayMapData[dayVal]['ip'][el]
        xVal = float(ipEl['x'])
        yVal = float(ipEl['y'])
        # print(el)
        # print(xVal)
        # print(yVal)
        if not el in regressionLineMap:
            regressionLineMap[el]= []

        yIntercept = float(slope)*xVal + float(intercept)
        diff = abs(yVal - yIntercept)
        regressionLineMap[el].append(diff)

print('Regression Calculated')
# for el in regressionLineMap:
    # print("{},{}".format(el,regressionLineMap[el]))
for ipVal in regressionLineMap:
    arr = regressionLineMap[ipVal]
    # print(arr)
    stdDev = 0
    if len(arr) >2:
        stdDev = statistics.stdev(arr)
    writeFile.write("{},{}".format(ipVal,"##".join([str(x) for x in arr])))
    writeFile.write("\n")
    writeFile.flush()














