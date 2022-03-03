import pandas as pd
import os
os.system('clear')
#Creating Pandas DataFrame

data = {'name': ['Aarian', 'Peter'],
'age': [18,20]}

df = pd.DataFrame(data)
print(df)

listBig = [["Peter", 20],["Sherry", 12],["Chris", 40]]
df1 = pd.DataFrame(listBig, columns=["name","age"])

print(df1)

#Reading from csv file

df3 = pd.read_csv("insurance_data.csv")

print(df3)