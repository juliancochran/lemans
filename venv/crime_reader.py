#import pandas
import csv
from datetime import datetime

#df = pandas.read_csv('Chicago_Crimes_2012_to_2017.csv')
#print(df)

'''file = open('Chicago_Crimes_Oct_2012_Jan_2017.csv', 'w')'''
crimes = []
header = ['','ID','Case Number','Date','Block','IUCR','Primary Type','Description','Location Description','Arrest','Domestic','Beat','District','Ward','Community Area','FBI Code','X Coordinate','Y Coordinate','Year','Updated On','Latitude','Longitude','Location']


with open('Chicago_Crimes_2012_to_2017.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    start = datetime.strptime('10/01/2012', '%m/%d/%Y')
    stop = datetime.strptime('01/01/2017', '%m/%d/%Y')
    for row in csv_reader:
        try:
            datetime_obj = datetime.strptime(row[3], '%m/%d/%Y %I:%M:%S %p')
            if start < datetime_obj < stop:
                crimes.append(row)
        except:
            continue
crimes.sort(key=lambda x: datetime.strptime(x[3], '%m/%d/%Y %I:%M:%S %p'))
with open('crimes.csv', 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)

    for row in crimes:
        csv_writer.writerow(row)

print('finished')