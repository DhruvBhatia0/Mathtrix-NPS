'''
Death rates for each possible combination of diseases
authors: Dhruv Bhatia, Ishaan Mishra
17th November, 2020
'''

import csv

L = []
with open('COVID_Dataset.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        L.append(row)
print(len(L), 'is the cardinality of the dataset')


def checkbelike(t1, t2, t3):
    global L
    ded = 0
    total = 0
    for i in L:

        if i[5] == str(t1) and i[6] == str(t2) and i[7] == str(t3):
            total += 1
            if i[8] == 'Dead':
                ded += 1

    rate = ded / total * 100
    if t1 == t2 == t3 == False:
        print('  No pre-existing condition:', round(rate, 2), '%')

    else:
        st = ''
        if t1 == True:
            st += '  Diabetes '
        if t2 == True:
            st += '  Abnormal_BP '
        if t3 == True:
            st += '  Respiratory_Illness '
        st += ':'
        print(st, round(rate, 2), '%')


tval = [
    [True, True, True],
    [True, True, False],
    [True, False, True],
    [True, False, False],
    [False, True, True],
    [False, True, False],
    [False, False, True],
    [False, False, False]]

print('Death Rates With :')
for i in tval:
    checkbelike(i[0], i[1], i[2])
