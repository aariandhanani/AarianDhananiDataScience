import pandas as pd
import os
os.system('clear')
#Creating Pandas DataFrame

data = {'name': ['Aarian', 'Peter'],
'age': [18,20]}

df = pd.DataFrame(data)
print(df)