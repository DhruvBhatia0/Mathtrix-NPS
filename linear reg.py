'''two strings need to be imported from the dataset
one, the first is x, which acts as the x axis
the other is the y axis
the x and y axes' arguments have to be lists
i have passed them both as method params'''
import csv
import healthDataEditable as hd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn import linear_model

resultAge = resultDis = result = 0


def linReg(tup, pred, n):  # n is the number of independent variables
    global resultAge
    global resultDis
    global result
    X = tup[0]
    y = tup[1]

    # print(X)
    # polynomial_features = PolynomialFeatures(degree=5)

    # XT = polynomial_features.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)
    model = linear_model.LinearRegression()

    model.fit(X_train, y_train)

    # regression coefficients
    # print('Coefficients: \n', model.coef_)

    # print('Variance score: {}'.format(model.score(X_test, y_test)))
    if n == 3:
        pred1 = np.array(pred).reshape(-1, 3)
        # pred1_t=polynomial_features.fit_transform(pred)
        resultDis = model.predict(pred)
        # print(resultDis)
    elif n == 1:
        pred1 = np.array(pred).reshape(-1, 1)
        # pred1_t=polynomial_features.fit_transform(pred)
        resultAge = model.predict(pred)
        # print(resultAge)

    elif n == 4:
        pred1 = np.array(pred).reshape(-1, 4)
        # pred1_t=polynomial_features.fit_transform(pred)
        result = model.predict(pred)
        # print(result)

    return (resultDis, resultAge, result)

    # pred1=np.array(pred2).reshape(1,-1)
    # print(model.predict(pred))


''' model=LinearRegression().fit(x,y)
    #a tuple is returned from this method
    #t[0]=R^2, t[1]=intercept and t[2]=slope
    #print("hello")
    t=(model.intercept_,model.coef_,model.predict(pred))'''


# return t

def makeTupleList(n1, n2, name):
    l = hd.getColumn(n1, name)
    l2 = hd.getColumn(n2, name)
    dis = hd.getDiseases(name)
    # print(dis)
    l3 = dis[0]
    l4 = dis[1]
    l5 = dis[2]
    lt = []
    l1 = []
    # print(l)
    for i in range(len(l)):
        # print(type(l[i]))
        val = int(l[i]) / 10
        l1.append(val)
    for i in range(len(l1)):
        val = None
        if l2[i][0] == "A":
            val = 1
        else:
            val = 0
        # print(l1[i])
        # print(type(l1[i]))
        lt.append((l1[i], val, l3[i], l4[i], l5[i]))
        # print(lt)
    return lt


def getArrayDiseases(t):
    # print(t)
    arrx, arry = [], []
    x1, x2, x3, x4, x5 = [], [], [], [], []
    for i in t:
        # x1.append(i[0])#age
        x2.append(i[1])  # dead or alive
        x3.append(i[2])  # diabeles
        x4.append(i[3])  # resp
        x5.append(i[4])  # bp
    arry = x2

    for i in range(len(x2)):
        arrx.append([x3[i], x4[i], x5[i]])  # array having data of diseases

    # print(arrx)
    x = np.array(arrx).reshape(-1, 3)
    y = np.array(arry)

    return (x, y)


def getArrayAge(t):
    arrx, arry = [], []
    x1, x2 = [], []
    for i in t:
        x1.append(i[0])  # age
        x2.append(i[1])  # dead or alive

    arry = x2
    arrx = x1

    x = np.array(arrx).reshape(-1, 1)
    # print(x)
    y = np.array(arry)

    return (x, y)


def getArray(t):
    # print(t)
    arrx, arry = [], []
    x1, x2, x3, x4, x5 = [], [], [], [], []
    for i in t:
        x1.append(i[0])  # age
        x2.append(i[1])  # dead or alive
        x3.append(i[2])  # diabeles
        x4.append(i[3])  # resp
        x5.append(i[4])  # bp
    arry = x2

    for i in range(len(x1)):
        arrx.append([x1[i], x3[i], x4[i], x5[i]])

    # print(arrx)
    x = np.array(arrx).reshape(-1, 4)
    y = np.array(arry)

    return (x, y)


def implement(n1, n2, pred1, pred2, pred3, name="COVID_Dataset.csv"):
    global resultAge
    global resultDis
    global result
    l = makeTupleList(n1, n2, name)
    t1 = getArrayDiseases(l)
    t2 = getArrayAge(l)
    t3 = getArray(l)
    res1 = linReg(t1, [pred1], 3)  # pred1 is list of diseases
    res2 = linReg(t2, [pred2], 1)  # pred 2 is list containing age
    res3 = linReg(t3, [pred3], 4)  # pred 3 is list containing age and diseases
    # print(t1)

    return (float(resultDis), float(resultAge), float(result))


# print(implement(5,9,[0,1,0],[20],[20,0,1,0]))

'''def getInfo():
    arr1=hd.getDiseases()
    temp=hd.getColumn(5)
    arr2=[]

    #for i in temp:
        #n=i/10
        #arr2.append(n)'''
'''def quicksortbelike(l):
    length=len(l)
    if length<=1:
        return l
    else:
        pivot=l.pop()
    itemg=[]
    iteml=[]
    for item in l:
        if item[0] > pivot[0]:
            itemg.append(item)
        else:
            iteml.append(item)
    return quicksortbelike(iteml) + [pivot] + quicksortbelike(itemg)
def selSort(l):
    for i in range(len(l)):
        dat=l[i][0]
        ind=i
        for j in range(i+1,len(l)):
            if l[j][0]<dat:
                dat=l[j][0]
                ind=j
        l[ind],l[i]=l[i],l[ind]'''