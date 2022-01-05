'''two strings need to be imported from the dataset
one, the first is x, which acts as the x axis
the other is the y axis
the x and y axes' arguments have to be lists
i have passed them both as method params'''
import csv
import healthDataEditable as hd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model

def linReg(tup,pred=[40,1,0,1]):
    X=tup[0]
    y=tup[1]
    print(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,random_state=1)
    model = linear_model.LinearRegression()
    
    model.fit(X_train, y_train) 
  
    #regression coefficients 
    print('Coefficients: \n', model.coef_) 
   
    print('Variance score: {}'.format(model.score(X_test, y_test)))

    pred=np.array(pred).reshape(-1,4)
    print(model.predict(pred))
    
    '''
    model=LinearRegression().fit(x,y)
    #a tuple is returned from this method
    #t[0]=R^2, t[1]=intercept and t[2]=slope
    #print("hello")
    t=(model.intercept_,model.coef_,model.predict(pred))'''
    #return t

def makeTupleList(n1,n2,name):
    l=hd.getColumn(n1,name)
    l2=hd.getColumn(n2,name)
    dis=hd.getDiseases(name)
    #print(dis)
    l3=dis[0]
    l4=dis[1]
    l5=dis[2]
    lt=[]
    l1=[]
    #print(l)
    for i in range(len(l)):
        #print(type(l[i]))
        val=int(l[i])/10
        l1.append(val)
    for i in range(len(l)):
        val=None
        if l2[i][0]=="A":
            val=1
        else:
            val=0
        #print(l1[i])
        #print(type(l1[i]))
        lt.append((l1[i],val,l3[i],l4[i],l5[i])) 
    #print(lt)
    return lt
def getArray(t):
    #print(t)
    arrx,arry=[],[]
    x1,x2,x3,x4,x5=[],[],[],[],[]
    for i in t:
        x1.append(i[0])#age
        x2.append(i[1])#dead or alive
        x3.append(i[2])#diabeles
        x4.append(i[3])#resp
        x5.append(i[4])#bp
    arry=x2
    
    for i in range(len(x1)):
        arrx.append([x1[i],x3[i],x4[i],x5[i]])
    
   # print(arrx)
    x=np.array(arrx).reshape(-1,4)
    y=np.array(arry)
    
    return (x,y)


def implement(n1,n2,name="COVID_Dataset.csv"):
    l=makeTupleList(n1,n2,name)
    t=getArray(l)
    t1=linReg(t)
    #print(t1)
    return
implement(5,9)


                ind=j
        l[ind],l[i]=l[i],l[ind]'''
