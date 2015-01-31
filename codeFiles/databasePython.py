__author__ = 'devashishthakur'

fileOpen = open("/Users/devashishthakur/Desktop/database-windows.csv")
idMarksMap = {}

for el in fileOpen:
    arr = el.rstrip().split(",")
    extraCredits = 0
    # print("{} = {} , {}".format(arr[0],len(arr),arr))
    if len(arr) >= 11:
        if arr[10] != '':
            # print('Extra credits obtained for {}  ={} '.format(arr[0],arr))
            extraCredits = arr[10]

    arr = arr[0:11]
    arr = arr[:-1]


    id = arr[0]
    midTermVal = arr[4]
    finalExamVal = arr[-1]

    new_arr = arr[1:4]
    for el in arr[5:-1]:
        new_arr.append(el)

    idMarksMap[id] = {}
    idMarksMap[id]['mid'] = midTermVal
    idMarksMap[id]['final'] = finalExamVal
    idMarksMap[id]['assignMarks'] = sorted(new_arr[:6])
    temp_arr = []
    for el in new_arr:
        if el.strip() == '' or el.strip() == 'Abs':
            temp_arr.append(0)
        else:
            temp_arr.append(float(el))

    new_arr = temp_arr

    new_arr = [float(x) for x in new_arr]
    # print("{} = {}".format(id,new_arr))
    new_arr[0] = new_arr[0]/100
    new_arr[1] = new_arr[1]/100
    new_arr[2] = new_arr[2]/100
    new_arr[3] = new_arr[3]/150
    new_arr[4] = new_arr[4]/100
    new_arr[5] = new_arr[5]/100
    new_arr[6] = new_arr[6]/140
    # print("{} = {}".format(id,new_arr))
    new_arr = sorted(new_arr,reverse=True)[:6]
    # print("{} = {}".format(id,sorted(new_arr[:6],reverse=True)))

    idMarksMap[id]['assignMarks'] = sorted(new_arr,reverse=True)[:6]

    idMarksMap[id]['assignSum'] = sum([float(x) for x in new_arr])
    idMarksMap[id]['assignAvg'] = sum(new_arr)/len(new_arr)
    idMarksMap[id]['assignAvg'] = idMarksMap[id]['assignAvg']*50

    idMarksMap[id]['total'] = (idMarksMap[id]['assignAvg']) + (float(idMarksMap[id]['mid']) * .25) + (float(idMarksMap[id]['final']) * .20)
    idMarksMap[id]['extraCredits'] = extraCredits
    idMarksMap[id]['total'] += float(extraCredits)

idMarksVal = {}
for el in idMarksMap:
    idMarksVal[el] = idMarksMap[el]['total']
    print('{} = {}'.format(el,idMarksMap[el]))

sorted_val = sorted(idMarksVal.items(),key=lambda x : x[1],reverse=False)
count = 1
for el in sorted_val:
    print('{}. {} = {}'.format(count,el[0],el[1]))
    count += 1


# print(idMarksMap[0589])