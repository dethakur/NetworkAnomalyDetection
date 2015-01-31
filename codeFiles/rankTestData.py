__author__ = 'devashishthakur'
import networkx as nx
import pickle
import rpyExample
import time
import scipy
from time import strptime
import decimal

from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import precision_recall_curve

accDataSet=[]
mostFrequentDataSet=[]
predictedDataSet=[]

dayWiseData = pickle.load(open("../pickle/dayWiseTestData.pkl","rb"))
ipMapData = pickle.load(open("../pickle/ipMapTestData.pkl","rb"))

def values_From_duration(timeStr):
    y = time.strptime(timeStr,"%H:%M:%S")
    hour = y.tm_hour
    min = y.tm_min
    sec = y.tm_sec
    return (int(hour)*60 + int(min))*60 + sec

ipRankMap = pickle.load(open("../pickle/ipRankMapTestData.pkl","rb"))
PrecitedAnomalousIpMap = {}
rankChangeArr = {}
for el in ipRankMap:
    arr = ipRankMap[el]

    if len(arr) > 2:
        changeArr = rpyExample.estimate_cp_r_(arr, penalty_value = 0.81)
        if len(changeArr) != 0:
            rankChangeArr[el]=True


errorIp = pickle.load(open("../pickle/flaggedIps.pkl","rb"))


errorIpKeys = list(errorIp.keys())

errorIpKeys = {}

for el in ipRankMap:
    if len(ipRankMap[el]) < 2:
        del ipMapData[el]

no_of_lines = 0
for x in ipMapData:
    no_of_lines+=len(ipMapData[x])

print('Number of lines = ',no_of_lines)

for el in errorIp:

    if el not in ipRankMap:
        continue

    if len(ipRankMap[el]) > 2:
        # print("{} = {}".format(el,len(ipMapData[el])))
        errorIpKeys[el] = True

print("Number of dat = ",len(dayWiseData.keys()))

print('Length of the entire data set = ',len(ipMapData.keys()))
print('Length of the anomalies = ',len(errorIpKeys.keys()))
print('Length of anomalies predicted = ',len(rankChangeArr.keys()))
print('Length of anomalies which are anomalies = ',len(set(errorIpKeys).intersection(set(rankChangeArr))))
print('Length of anomalies which are not anomalies = ',len(set(rankChangeArr) - set(errorIpKeys)))

accDataSet=[]
mostFrequentDataSet=[]
predictedDataSet=[]

indexCount = 0
for key in ipMapData.keys():
    if key in rankChangeArr:
        predictedDataSet.append(1)
    else:
        predictedDataSet.append(0)

    if key in errorIpKeys:
        accDataSet.append(1)
    else:
        accDataSet.append(0)

    mostFrequentDataSet.append(1)

count = 0
from collections import Counter
print(Counter(accDataSet))
print(Counter(mostFrequentDataSet))
print(Counter(predictedDataSet))

# print('Predicted Average precision score  - ',average_precision_score(accDataSet,predictedDataSet))

precision, recall, thresholds = precision_recall_curve(
    accDataSet,predictedDataSet)

print('Precision score = ',precision)
print('Recall = ',recall)
print('Threshold = ',thresholds)
print('Predicted precision score  - ',precision_score(accDataSet,predictedDataSet))
print('Predicted recall score  - ',recall_score(accDataSet,predictedDataSet))

# print('Most Frequent average Prediction precision score  - ',average_precision_score(accDataSet,mostFrequentDataSet))
print('Most Frequent Prediction precision score  - ',precision_score(accDataSet,mostFrequentDataSet))
print('Most Frequent recall score  - ',recall_score(accDataSet,mostFrequentDataSet))
setval = set()
completeSet = set()

# for line in ipMapData:
#     for el in ipMapData[line]:
#         arr = el.split()
#         if arr[len(arr)-1] != '-':
#             completeSet.add(arr[len(arr)-1])
#
# for ip in rankChangeArr:
#     line = ipMapData[ip]
#     for el in line:
#         arr = el.split()
#         if arr[len(arr)-1] != '-':
#             setval.add(arr[len(arr)-1])
#             # break
#     # break
# print('Length of anomalies ')
# completeSet = completeSet - setval
# for el in completeSet:
#     print(el)
ipToSizeMap = {}
# for el in rankChangeArr:
#     for line in ipRankMap[el]:
#        ipToSizeMap[el] = len(ipRankMap[el])
#
# sorted_val = sorted(ipToSizeMap.items(),key=lambda x: x[1],reverse=True)
# for el in sorted_val:
#     print("{} = {} = {}".format(el[0],el[1],ipRankMap[el[0]]))



# print(accDataSet)
# print(mostFrequentDataSet)
# print(predictedDataSet)

