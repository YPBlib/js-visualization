import csv
from pathlib import Path
p = Path('./data')
cnt=0
lng_max=-1
lng_min=1e8
lat_max=-1
lat_min=1e8
with open('coordinate.txt','w') as f:
    for x in p.iterdir():
        with  open(x,newline='',encoding='UTF-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #        print(dir(spamreader))
            for row in spamreader:
                if row[0]!='md5':
                    lng=float(row[5])
                    lat=float(row[6])
                    f.write(row[5])
                    f.write(' ')
                    f.write(row[6])
                    f.write('\n')
                       
print(cnt,lng_min,lng_max,lat_min,lat_max,sep='\n')

#with  open('data/test.csv',encoding='UTF-8') as f:
#    for i in f:
#        print(i)

