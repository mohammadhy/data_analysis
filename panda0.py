
"""
Created on Wed Sep  2 12:03:31 2020

@author: Asus
"""

import pandas as pd
import numpy as np
x = {
     'name':['ali', 'hassan', 'hossein', 'omid' , 'mehdi', 'shahin', 'sorosh'],
     'age':[12, 15, 25, 36, 52, 42 ,18],
     'salary':[1000, 3000, 1500, 2500, 1800, 6500, 4200]
     }



df = pd.DataFrame(x)
'''
Read some column: 
------------------------------
print(df[['name', 'age']][1:5])
'''


'''
Set My Index:
------------------------------
df = df.set_index(['name'])
'''

'''
Read Specific Row By Iloc:
------------------------------
for index, row in df.iterrows():
	print(index, row['salary'])
print(df.iloc[-1, 2])
'''

'''
Find Specific Name Or Age :
----------------------------
print(df.loc[df['age'] == 25])
'''

'''
Report Of Data:
----------------------------------
print(df.describe())
'''

'''
Sort By Little To High And Vice_Versa:
-----------------------------------
print(df.sort_values('age', ascending = False))
'''

'''
Creat And Delete  Column:
------------------------------------
df['info'] = df['salary'] + df['age']
print(df)
print(df)
df.drop(columns=['name'], inplace=True, axis=0)
print(df)
'''

'''
Define New Column By Specific Paramiter:
-----------------------------------------
df['info'] = df.iloc[0:4,0:2].sum(axis=1)
print(df)
'''

'''
Organize The Column:
----------------------------------------
col = list(df.columns)
print(col)
df = df[col[1:2] + [col[-1]]]
print(df)
'''





#y = np.array(df)

#for i in y:
#    print(i)