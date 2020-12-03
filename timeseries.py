#python3.8.5

"""
Created on Sun Nov 15 18:54:54 2020

@author: HY
"""
import pandas as pd 
from datetime import datetime
import numpy as np 
import matplotlib.pyplot as plt

index = pd.date_range('2020-01-01', '2021-01-01')


data = np.random.randn(367, 4)

df = pd.DataFrame(data, index=index)
df.rename(columns={0:'iphone11 pro', 1:'iphone12', 2:'macbook', 3:'appletv'}, inplace=True)
best_sell = df.asfreq(freq='BM')

best_sell = best_sell.replace(to_replace =best_sell['iphone11 pro'].values, 
                 value =np.random.randint(2, size=12))

#df['employrate'] = np.where(
#   (df['employrate'] <=55) & (df['employrate'] > 50) , 11, df['employrate'])


