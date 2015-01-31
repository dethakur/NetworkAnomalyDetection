import matplotlib.pyplot as plt
import matplotlib.lines as lines

x1 = "0.0022611860061051313, 2.6297662616384005e-05, 0.04554907038158084, 0.0011210762331838565, 0.00264605945964271, 0.0012594458438287153, 0.001472336506842383"
x2 = "2.9918959360525375e-05, 0.00023118595541051022, 0.02344374610873865, 0.002709402400179199, 0.00013552693594205033, 0.00026940387266218333"
x3 ="2.9918959360525375e-05, 0.0002650638115747285, 0.02344374610873865, 0.00022415326299657124, 0.00026715463187271173, 9.366578759026844e-05"
x4 ="3.925422729947567e-05, 0.00020124932371382427, 0.02344374610873865, 0.00022415326299657124, 0.00026715463187271173, 9.366578759026844e-05"
x5 ="2.6297662616384005e-05, 0.0011068210243574176, 0.23807006163806424, 0.0003140590155493954"
x6 ="0.00018628100786548132, 0.008901477067725205, 0.0001774934063140773, 0.10304949441356225, 9.366578759026844e-05"
x7 ="0.001943731317295153, 0.001714893263346762, 0.0016042505096354315, 0.0018444070068464387, 0.0017494032567925049, 0.0007549603901281354, 0.002028320259240552, 0.0015288005790292463, 0.0011572331812556877"
x8 = "0.01188868936886232, 0.027188979922794933, 0.0024193227527393273, 0.0074244061991971064, 0.016882947058256582, 0.005153509929630759, 0.011047320882164414, 0.017313600780222815, 0.006524375907068934"
arr = x1.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,1)
plt.plot(xAxis,yAxis)
plt.title("Anomalous IP")

arr = x2.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,2)
plt.plot(xAxis,yAxis)
plt.title("Anomalous IP")

arr = x3.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,3)
plt.plot(xAxis,yAxis)
plt.title("Anomalous IP")

arr = x4.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,4)
plt.plot(xAxis,yAxis)
plt.title("Anomalous IP")

arr = x5.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,5)
plt.plot(xAxis,yAxis)
plt.title("Anomalous IP")

arr = x6.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,6)
plt.plot(xAxis,yAxis)
plt.title("Anomalous IP")

arr = x7.split(",")
xAxis = range(len(arr))
yAxis = arr
plt.subplot(4,2,7)
plt.plot(xAxis,yAxis)
plt.title("Normal IP")

arr = x8.split(",")
xAxis = range(len(arr))
yAxis = arr
axes2 = plt.gca()
axes2.set_ylim([0,.04])
plt.subplot(4,2,8)
plt.plot(xAxis,yAxis)
plt.title("Normal IP")


axes2 = plt.gca()
axes2.set_ylim([0,.10])

plt.show()
# plt.subplot(4,3,2)