'''
Vital info by grid
author: Ishaan Mishra, Dhruv Bhatia
18th November, 2020
'''

# ------------------------INITIALISING------------------------#
import csv

L = []
G = []
GI = []
grid_width = 20
grid_length = 20


# ------------------------SETUP------------------------#

class stats:
    '''
    STATISTICS-
    population, infections, deaths, death rate, [disease wise death rate],
    [age wise death rate], time lag
    '''

    def __init__(self):
        self.pop = 0
        self.inf = 0
        self.deds = 0
        self.dr = 0
        self.DD = []
        self.DA = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.t = 0
        self.irate = 0
        self.lagscore = 0
        self.x = 0
        self.y = 0

    def display_data(self):
        print(self.pop, self.inf, self.deds, self.dr, self.DD, self.DA, self.t, self.irate)

    def displa_location(self):
        pass


with open('COVID_Dataset.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        L.append(row)

totalpop = 0
total = stats()
pop = []
with open('Population.csv', 'r') as f:
    c = 0
    reader = csv.reader(f)
    for row in reader:
        if c != 0:
            pop.append(row[2])
        c += 1

checklist = []
counter = 0
for i in range(grid_width):
    g = []
    for j in range(grid_length):
        k = stats()
        k.pop = int(pop[counter][:-2])
        k.x = i
        k.y = j
        if [k.x, k.y] in checklist:
            print([k.x, k.y])
        checklist.append([k.x, k.y])
        totalpop += int(pop[counter][:-2])
        g.append(k)
        counter += 1
    G.append(g)

total.pop = totalpop

for i in range(grid_width):
    g = []
    for j in range(grid_length):
        g.append([])
    GI.append(g)
c = 0
for i in L:
    if c != 0:
        GI[int(i[2]) - 1][int(i[3]) - 1].append(i)
    c += 1

tval = [
    [True, True, True],
    [True, True, False],
    [True, False, True],
    [True, False, False],
    [False, True, True],
    [False, True, False],
    [False, False, True],
    [False, False, False]]


# ------------------------FUNCTIONS------------------------#

def checkbelikeage(L, DA):
    L[4] = int(L[4])
    b1, b2, b3, b4, b5 = DA
    if L[4] <= 10:
        b1[1] += 1
        if L[8] == 'Dead':
            b1[0] += 1
    elif L[4] <= 20:
        b2[1] += 1
        if L[8] == 'Dead':
            b2[0] += 1
    elif L[4] <= 40:
        b3[1] += 1
        if L[8] == 'Dead':
            b3[0] += 1
    elif L[4] <= 60:
        b4[1] += 1
        if L[8] == 'Dead':
            b4[0] += 1
    elif L[4] > 60:
        b5[1] += 1
        if L[8] == 'Dead':
            b5[0] += 1
    return ([b1, b2, b3, b4, b5])


def checkbelikedisease(t1, t2, t3, L):
    ded = 0
    total = 0
    for i in L:
        if i[5] == str(t1) and i[6] == str(t2) and i[7] == str(t3):
            total += 1
            if i[8] == 'Dead':
                ded += 1
    if total == 0:
        rate = -1  # if there is no one with the diseases infected in the area
    else:
        rate = round(ded / total * 100, 2)

    return (rate)


cellcount = 1


def calc_stats(L, stats):
    global cellcount
    global tval
    c = 0

    for j in tval:
        stats.DD.append(checkbelikedisease(j[0], j[1], j[2], L))
    for i in L:

        if c != 0:
            checkbelikeage(i, stats.DA)
            stats.inf += 1
            if i[8] == 'Dead':
                stats.deds += 1
            '''for j in tval:
                stats.DD.append(checkbelikedisease(j[0],j[1],j[2], L))
            stats.DA=checkbelikeage(i, stats.DA)'''
            stats.t += (int(i[1]) - int(i[0])) / len(L)
        r = stats.deds / (stats.pop) * 100
        stats.sr = round(r, 2)
        c += 1
    stats.t = round(stats.t, 2)
    stats.irate = round(stats.inf / stats.pop * 100, 2)
    if stats.inf == 0:
        stats.dr = -1
    else:
        stats.dr = round(stats.deds / stats.inf * 100, 2)
    for i in range(len(stats.DA)):
        if stats.DA[i][1] == 0:
            stats.DA[i] = -1
        else:
            stats.DA[i] = round(stats.DA[i][0] / stats.DA[i][1] * 100, 2)

    stats.lagscore = (50 + stats.irate) * stats.t
    # testing(c1)print(stats.lagscore)
    # print(cellcount, 'calculated')
    cellcount += 1


# ------------------------DATA_COLLECTION------------------------#
tetet = 0

for i in range(grid_width):
    for j in range(grid_length):
        calc_stats(GI[i][j], G[i][j])

calc_stats(L, total)
G[12][7].display_data()
total.display_data()

print('Well, it seems to be working')

# total.lagscore=total.irate*total.t
# print('avg:',total.lagscore)


# ------------------------DATA_INTERPRETATION------------------------#
'''
- c1: high cases, high lag = suggest testing [irate, t]
- c2: many old dedz, = improve health infra
- c3: irate high = implement lockdown
- c4: abnormally high death rate = check for varying strain
- c5: herd immunity distance time(60%)
'''

cc = 10

c1 = c2 = c3 = c4 = c5 = []


def testing():
    global total, G, c1
    for j in G:
        for i in j:
            if i.t >= total.t and i.irate > total.irate and i not in c1:
                c1.append(i)


testing()
for i in range(len(c1) - 1):
    for j in range(len(c1) - 1 - i):
        if c1[j].lagscore < c1[j + 1].lagscore:
            c1[j + 1], c1[j] = c1[j], c1[j + 1]
cf = []
for i in c1[:cc]:
    cf.append(i)
c1 = cf


def infrastructure():
    global total, G, c2
    for j in G:
        for i in j:
            if i.DA[4] >= total.DA[4] and i not in c2:
                c2.append(i)


infrastructure()
for i in range(len(c2) - 1):
    for j in range(len(c2) - 1 - i):
        if c2[j].DA[4] < c2[j + 1].DA[4]:
            c2[j + 1], c2[j] = c2[j], c2[j + 1]
cf = []
for i in c2[:cc]:
    if i not in cf:
        cf.append(i)
c2 = cf


def lockdown():
    global total, G, c3
    for j in G:
        for i in j:
            if i.irate >= total.irate and i not in c3:
                c3.append(i)


lockdown()
for i in range(len(c3) - 1):
    for j in range(len(c3) - 1 - i):
        if c3[j].irate < c3[j + 1].irate:
            c3[j + 1], c3[j] = c3[j], c3[j + 1]
cf = []
for i in c3[:cc]:
    cf.append(i)
c3 = cf


def strain():
    global total, G, c4
    for j in G:
        for i in j:
            if i.dr >= total.dr and i not in c4:
                c4.append(i)


strain()
for i in range(len(c4) - 1):
    for j in range(len(c4) - 1 - i):
        if c4[j].dr < c4[j + 1].dr:
            c4[j + 1], c4[j] = c4[j], c4[j + 1]
cf = []
for i in c4[:int(cc / 2)]:
    cf.append(i)
    print(i.dr)
# print('avg dr: ', total.dr)

c4 = cf


def herd_immunity():
    global total, G, c5
    for j in G:
        for i in j:
            if i.irate >= 60 and i not in c5:  # acc to WHO, herd immunity when infected between 50,90
                c5.append(i)


herd_immunity()
for i in range(len(c5) - 1):
    for j in range(len(c5) - 1 - i):
        if c5[j].irate < c5[j + 1].irate:
            c5[j + 1], c5[j] = c5[j], c5[j + 1]
cf = []
for i in c5:
    cf.append(i)
c5 = cf


# ------------------------RETURNING_INFO------------------------#

def cprint(c):
    coord = []
    for i in c:
        coord.append([i.x + 1, i.y + 1])
    for i in range(len(coord) - 1):
        for j in range(len(coord) - 1 - i):
            if coord[j][0] == coord[j + 1][0]:
                if coord[j][1] > coord[j + 1][1]:
                    coord[j + 1], coord[j] = coord[j], coord[j + 1]
            elif coord[j][0] > coord[j + 1][0]:
                coord[j + 1], coord[j] = coord[j], coord[j + 1]
    return (coord)


general = '''General Information:
Population: '''
general += str(total.pop) + '\nCases: '
general += str(total.inf) + '\nDeaths: '
general += str(total.deds) + '\nMortality Rate: '
general += str(total.dr) + '%\n\tMortality Rates by Age:\n\t'
general += '''0-10  : \t''' + str(total.DA[0]) + '''%
\t10-20 : \t''' + str(total.DA[1]) + '''%
\t20-40 : \t''' + str(total.DA[2]) + '''%
\t40-60 : \t''' + str(total.DA[3]) + '''%
\t>60   : \t''' + str(total.DA[4]) + '%'