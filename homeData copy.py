#Aarian Dhanani
#1/25/2022
#Find a CSV data set and prepare it for a study: Explain your reasoning of the fields to change, add or eliminate

import os
os.system('clear')

import csv
file = open('home_data.csv')
homeFile = csv.reader(file)
header = next(homeFile)
print(header)
houseData = []
for row in homeFile:
    row.append(homeFile)
    houseData.append(row)
    print(row)