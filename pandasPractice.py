import pandas as pd
import os
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
print(dfInsurance)
dfInsurance["cost"] = ((float(dfInsurance['age']))*250) - ((dfInsurance['sex'])*250)
dfInsurance["cost"] = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500