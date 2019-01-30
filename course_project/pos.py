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

for i in range(100):
    for j in range(100):
        print(mat[i][j],end=' ')
    print('\n')
        
