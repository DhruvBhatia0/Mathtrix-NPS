''' this module will be used to extract data from given csv dataset and will
generate each record and each column of data
usage:

print(getColumn(fieldHeadings()['Population']))'''

import csv

records=[]
columns=[]

def fieldHeadings():
    fieldDict={'x location':1,'y location':2,'Population':3}
    return fieldDict
    
def getRecord():
    global records
    with open('C:\\Users\\Humans\\Documents\\My Docs-Disha\\py\\mathrix2020\\Population.csv','r+') as csvfile:
    #with open("C:\\Users\\Humans\\Documents\\My Docs-Disha\\py\\mathrix2020\\emp.csv","r+") as csvfile:
        reader=csv.reader(csvfile)
        for i in reader :
            if i!=[]:
                records.append(i)
    return records
        
        

def getColumn(colnum):
    global columns
    global records
    getRecord()
    
    for i in records:
        columns.append(i[colnum-1])
    return columns[1::]

print(getColumn(fieldHeadings()['Population']))
