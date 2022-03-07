import pandas as pd
import os
os.system('clear')
#Creating Pandas DataFrame

# data = {'name': ['Aarian', 'Peter'],
# 'age': [18,20]}

# df = pd.DataFrame(data)
# #print(df)

# listBig = [["Peter", 20],["Sherry", 12],["Chris", 40]]
# df1 = pd.DataFrame(listBig, columns=["name","age"])

# print(df1)

# #Reading from csv file

# dfInsurance = pd.read_csv("insurance_data.csv")
# #print(df3)
# df2 = dfInsurance[(dfInsurance['age'] > 20) & (dfInsurance['smoker']=='yes')]
# print(df2)







df=pd.DataFrame([ 
    ['Aarian','Assignment 1',100],
    ['Aarian','Assignment 2',90],
    ['Aarian','Assignment 3',98],
    ['Aarian','Assignment 4',95],
    ['Aarian','Assignment 5',100],
    ['Steven','Assignment 1',90],
    ['Steven','Assignment 2',95],
    ['Steven','Assignment 3',98],
    ['Steven','Assignment 4',100],
    ['Steven','Assignment 5',90],
], 
columns = ["Name","Assignment","Grade"])

print(df.groupby('Name').Grade.mean())
print(df.groupby('Name').Grade.std())
print(df.groupby('Name').Grade.median())
print(df.groupby('Name').Grade.count())