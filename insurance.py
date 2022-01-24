#Aarian Dhanani
#1/24/2022
#Prepare a dataset using a csv file by changing female/male and smoker/non smoker to 1 and 0

import os
os.system('clear')

import csv
file = open('insurance_data.csv')
print(type(file))
insuranceFile = csv.reader(file)
header = next(insuranceFile)
print(header)
insuranceData = []
for row in insuranceFile:
    if(row[1] == "female"):
        row[1] = 0
    else:
        row[1] = 1
    
    if(row[4] == "smoker"):
        row[4] = 1
    else:
        row[4] = 0
    
    insurance_cost = (250*float(row[0])) - (128*float(row[1])) + (370*float(row[2])) + (425*float(row[3])) + (24000*float(row[4])) - 12500
    insurance_cost = int(insurance_cost*100)/100
    row.append(insurance_cost)
    insuranceData.append(row)
    print(row)


#Calculate location insurance cost averages
NETotal = 0
NENumber = 0
NWTotal = 0
NWNumber = 0
SETotal = 0
SENumber = 0
SWTotal = 0
SWNumber = 0
for row in insuranceData:
    if(row[5] == "northeast"):
        NETotal = NETotal + float(row[7])
        NENumber = NENumber + 1
    if(row[5] == "northwest"):
        NWTotal = NWTotal + float(row[7])
        NWNumber = NWNumber + 1
    if(row[5] == "southeast"):
        SETotal = SETotal + float(row[7])
        SENumber = SENumber + 1
    if(row[5] == "southwest"):
        SWTotal = SWTotal + float(row[7])
        SWNumber = SWNumber + 1

print("Northeast average: " + str(NETotal/NENumber))
print("Northwest average: " + str(NWTotal/NWNumber))
print("Southeast average: " + str(SETotal/SENumber))
print("Southwest average: " + str(SWTotal/SWNumber))


#Create female and male lists
femaleInsuranceData = []
maleInsuranceData = []
for row in insuranceData:
    if(row[1] == 0):
        femaleInsuranceData.append(row)
    else:
        maleInsuranceData.append(row)


#Create smoker and non-smoker lists
nonSmokerInsuranceData = []
smokerInsuranceData = []
for row in insuranceData:
    if(row[1] == 0):
        nonSmokerInsuranceData.append(row)
    else:
        smokerInsuranceData.append(row)