import pandas as pd
import os, csv
os.system('clear')

#Problem 1
df2=pd.DataFrame([ 
    [1,'San Diego',100],
    [2,'Los Angeles',120],
    [3,'San Fransisco',90],
    [4,'Sacramento',115],
    # Fill in rows 3 and 4
], 
columns = ["Store Number","City","Store ID"])
print(df2)

#Problem 2
df1=pd.DataFrame([ 
    [1,'t-shirt','blue'],
    [2,'t-shirt','green'],
    [3,'skirt','red'],
    [4,'skirt','black'],
    # Fill in rows 3 and 4
], 
columns = ["Product ID","Product Name","Color"])
print(df1)

#Problem 3
dfInsurance = pd.read_csv("insurance_data.csv")
dfInsurance["sex"].replace({"female":0,"male":1}, inplace=True)
dfInsurance["smoker"].replace({"no":0,"yes":1}, inplace=True)
dfInsurance["insurance cost"] = ((dfInsurance['age'])*250) - ((dfInsurance['sex'])*128) + ((dfInsurance['bmi'])*370) + ((dfInsurance['children'])*425) + ((dfInsurance['smoker'])*24000) - 12500
print(dfInsurance)

#Problem 4
df1.to_csv("df1.csv")