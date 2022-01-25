#Aarian Dhanani
#1/25/2022
#Find a CSV data set and prepare it for a study: Explain your reasoning of the fields to change, add or eliminate

from audioop import avg
import os
os.system('clear')

import csv
file = open('home_data.csv')
homeFile = csv.reader(file)
header = next(homeFile)
print(header)
houseData = []

#Max Floors: 3.5
#Max Waterfront: 1
#Max View: 4
#Max Condition: 5
#Max Grade: 13
#Max Bedrooms: 8
#Max Bathroooms: 8

avgPrice = 0.00
priceCounter = 0
avgSQFT = 0
avgLotSQFT = 0.00

for row in homeFile:
    #Remove ID
    row.pop(0)
    #Remove Date
    row.pop(0)
    #Remove Year Built
    row.pop(12)
    #Remove Year Renovated
    row.pop(12)
    #Remove Zipcode
    row.pop(12)
    #Remove Latitude
    row.pop(12)
    #Remove Longitude
    row.pop(12)
    #Remove Extra Info
    row.pop(12)
    #Remove Extra Info
    row.pop(12)

    totalSQFT = int(row[3]) + int(row[10]) + int(row[11])
    #print(totalSQFT)
    lotSQFT = row[4]
    # print(totalSQFT)
    # print(lotSQFT)

    if(float(row[1]) < 9):
        avgPrice = avgPrice + float(row[0])
        priceCounter = priceCounter + 1
        avgSQFT = int(avgSQFT) + int(totalSQFT)
        #print(avgSQFT)
        avgLotSQFT = float(avgLotSQFT) + float(lotSQFT)
        
        houseData.append(row)
        #print(row)

# print(int(avgPrice))
# print(priceCounter)
#print(avgSQFT)
print("Average House Price:", str((int(avgPrice/priceCounter))))
print("Average House SQFT:", str((int(avgSQFT/priceCounter))))
print("Average Lot SQFT:", str((int(avgLotSQFT/priceCounter))))