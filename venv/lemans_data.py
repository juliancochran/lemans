import csv
from driver import Driver
from team import Team
from racedata import Racedata
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from itertools import cycle, islice

races = []

with open('le_mans.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        drivers = []
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            '''for i in range(len(row)):
                print((str(i)+'-'+row[i].strip()), end=' ')
            dist = row[-1].split()
            print('\n',dist)'''
            num_drivers = int(row[1])
            # with either 2 or 3 drivers, there will be at least 2 drivers in the race
            drivers.append(Driver(row[3].split(), row[2]))
            drivers.append(Driver(row[5].split(), row[4]))
            try:
                if num_drivers == 3:
                    # 3 drivers, this will skew the indices for remaining data
                    #print('DEBUG 3 drivers:', row[0], row[13].strip())
                    drivers.append(Driver(row[7].split(), row[8]))
                    temp_team = Team(drivers, row[8], row[9], row[10], row[11])
                    dist = row[-1].split()
                    races.append(Racedata(int(row[0]), temp_team, int(row[-2]), float(dist[0])))
                else:
                    # 2 drivers
                    #print('DEBUG 2 drivers:', row[0], row[11].strip())
                    temp_team = Team(drivers, row[6], row[7], row[8], row[9])
                    dist = row[-1].split()
                    races.append(Racedata(int(row[0]), temp_team, int(row[-2]), float(dist[0])))
            except Exception as e:
                print(e)

# count car manufacturers and how many times they won
car_dictionary = {}
for race in races:
    if race.team.car_brand not in car_dictionary:
        car_dictionary[race.team.car_brand] = 1
    else:
        car_dictionary[race.team.car_brand] += 1

print('The following types of cars have won at Le Mans (number of times won):')

manufacturers = []
for key,val in list(car_dictionary.items()):
    manufacturers.append((val,key))
manufacturers.sort(reverse=True)
for key,val in manufacturers:
    print(val + ': ' + str(key) + (' times' if key != 1 else ' time'))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
major_ticks = np.arange(0,21,5)
minor_ticks = np.arange(0,21,1)
df = pd.DataFrame()
df['name'] = list(car_dictionary.keys())
df['value'] = list(car_dictionary.values())
df.sort_values('value', ascending=False,inplace=True)
my_colors = ('firebrick', 'darkred', 'red', 'darkorange', 'orange', 'gold', 'yellow', 'yellowgreen', 'green', 'teal', 'royalblue', 'blue', 'slateblue', 'darkviolet', 'purple', 'crimson')
plt.bar(range(len(car_dictionary)),df['value'], align='center', color=my_colors)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)
plt.xticks(range(len(car_dictionary)), df['name'], rotation=90)
ax.grid(which='both')
plt.show()