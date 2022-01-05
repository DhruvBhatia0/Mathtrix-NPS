''' this module will be used to extract data from given csv dataset and will
generate each record and each column of data'''

import csv
import codecs
records=[]
columns=[]
diseases=[]

def fieldHeadings():
    fieldDict={'Time of Infection':1,'Time of reporting':2,'x location':3,'y location':4,'Age':5,'Diabetes':6,'Respiratory Illnesses':7,'Abnormal Blood Pressure':8,'Outcome':9}
    return fieldDict
    
def getRecord(name):
    global records
    #with codecs.open(name, 'r', encoding='utf-32',errors='ignore') as csvfile:
    #with open('C:\\Users\\Humans\\Documents\\My Docs-Disha\\py\\mathrix2020\\COVID_Dataset.csv','r+') as csvfile:
    #with open("C:\\Users\\Humans\\Documents\\My Docs-Disha\\py\\mathrix2020\\emp.csv","r+") as csvfile:
    with open(name) as csvfile:
        reader=csv.reader(csvfile)
        #print(reader)
        try:
            
            for i in reader :
                if i!=[]:
                    records.append(i)
        except(UnicodeDecodeError):
            print("error")# print(records)
                
    return records
        
        

def getColumn(colnum,name):
    global columns
    global records
    columns=[]
    records=[]
    getRecord(name)
    
    for i in records:
        columns.append(i[colnum-1])
    return columns[1::]
        
def getDiseases(name):
    #function to get the number of diseases a patient suffers from
    global records
    records=[]
    diabetes=[]
    resp=[]
    bp=[]
    fieldDict=fieldHeadings()
    getRecord(name)
    for pat in records:
        num=0
        #converting data to 1/0
        #print(dict(fieldDict))
        #print(fieldDict['Diabetes'])
        #print(pat[fieldDict['Diabetes']])
        if pat[int(fieldDict['Diabetes'])-1]=='TRUE':
            
            #pat[fieldDict['Diabetes']-1]=1
            copy1=1
        else:
            #pat[fieldDict['Diabetes']]=0
            copy1=0
            
        if pat[fieldDict['Respiratory Illnesses']-1]=='TRUE':
            #pat[fieldDict['Respiratory Illness']]=1
            copy2=1
        else:
            #pat[fieldDict['Respiratory Illness']]=0
            copy2=0
        if pat[fieldDict['Abnormal Blood Pressure']-1]=='TRUE':
            #pat[fieldDict['Abnormal Blood Pressure']]=1
            copy3=1
        else:
            #pat[fieldDict['Abnormal Blood Pressure']]=0
            copy3=0
        
        diabetes.append(copy1)
        resp.append(copy2)
        bp.append(copy3)
        #temp=[pat[fielDict['Diabetes']],pat[fielDict['Respiratory Illness']],pat[fielDict['Abnormal Blood Pressure']]]
        '''temp=[copy1,copy2,copy3]
        for key in temp:
            num+=key
        diseases.append(num)'''

    return diabetes[1::],resp[1::],bp[1::]

#print(getColumn(9))
#print(getColumn(5,"COVID_dataset.csv"))

#print(getDiseases("COVID_Dataset.csv"))
#print(get("COVID_dataset.csv"))
 
