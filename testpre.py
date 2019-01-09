import csv
import re
from pathlib import Path
p = Path('./data')
cnt=0
lng_max=-1
lng_min=1e8
lat_max=-1
lat_min=1e8

with  open('data/test.csv',newline='',encoding='UTF-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#        print(dir(spamreader))
    for row in spamreader:
        print(type(row[0]),type(row[1]),type(row[2]),type(row[3]),type(row[4]),type(row[5]),type(row[6]))
        if row[0]!='md5':
            cnt+=1
            row[1]=row[1].rstrip()
            if float(row[5])>lng_max:
                lng_max=float(row[5])
            elif float(row[5])<lng_min:
                lng_min=float(row[5])
            if float(row[6])>lat_max:
                lat_max=float(row[6])
            elif float(row[6])<lat_min:
                lat_min=float(row[6])
print(cnt,lng_min,lng_max,lat_min,lat_max,sep='\n')

#with  open('data/test.csv',encoding='UTF-8') as f:
#    for i in f:
#        print(i)

