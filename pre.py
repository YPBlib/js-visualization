import csv
from pathlib import Path
p = Path('./data')
cnt=0
lng_max=-1
lng_min=1e8
lat_max=-1
lat_min=1e8
for x in p.iterdir():
    with  open(x,newline='',encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#        print(dir(spamreader))
        for row in spamreader:
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

