import csv
import numpy as np
from pathlib import Path
p = Path('./data')
cnt=[]
for i in range(100):
    cnt.append(0)


lng_max=117.48902130
lng_min=115.52557373
lat_max=40.96902084
lat_min=39.46577454

lng_delta=(lng_max-lng_min)/100.0
lat_delta=(lat_max-lat_min)/100.0

mat=np.zeros((100,100),dtype=float)
for x in p.iterdir():
    with  open(x,newline='',encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if row[0]!='md5':
                try:
                    x=int((float(row[5])-lng_min)/lng_delta)
                    y=int((float(row[6])-lat_min)/lat_delta)
                    mat[x][y]+=1
                except :
                   print(row[0],row[5],row[6],sep=' ')

class BTS:
    i=0
    j=0
    value=0
    def __init__(self,i,j,value):
        self.i=i
        self.j=j
        self.value=value

l=[]

for i in range(100):
    for j in range(100):
         l.append(BTS(i,j,mat[i][j]))


l.sort(key=lambda x:x.value,reverse=True)


s=[]


for i in range(300):
    s.append(l[i])

s.sort(key=lambda x:x.i)

for i in s:
    print('mat[{0}][{1}]'.format(i.i,i.j))

