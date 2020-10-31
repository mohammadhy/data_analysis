#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 09:51:39 2020

@author: hassan
"""

import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pylab as plt 

# load dataset data.csv
df = pd.read_csv('data.csv')
# change to lower case 
df.columns = df.columns.str.lower()
#we need car above 2015 
df['year'] = np.where(df['year'] > 2015, df['year'].values, np.nan)
# drop nan values
df.dropna(inplace=True) #you can use axis=1 but work on columns not row
#delet last 4 columns :
df = df.drop(columns=df.iloc[:, 12:])
# change all transmissin type to auto an manual :
df['transmission type'] =np.where(df['transmission type'].str.contains('AUTOMATIC'), 'automatic', 'manual')
# rename transmission type 
df.rename(columns={'transmission type':'transmission'},inplace=True)

data = pd.pivot_table(index='year', values='engine hp', columns='transmission', data=df)
x, data.value = np.modf(data.values)
data = data.reset_index()
sns.barplot(x='automatic', y='manual', hue='year', data=data)


