# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:41:26 2020

@author: Asus
"""
import pandas as pd
from datetime import datetime
data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
'age': [20, 19, 22, 21],
'favorite_color': ['blue', 'red', 'yellow', "green"],
'grade': [88, 92, 95, 70],
'birth_date': ['01-02-1996', '08-05-1997', '04-28-1996', '12-16-1995']}

df = pd.DataFrame(data)

df['year'] =pd.DatetimeIndex(df['birth_date']).year
df['month'] =pd.DatetimeIndex(df['birth_date']).month
df['day'] =pd.DatetimeIndex(df['birth_date']).day
df.drop('birth_date', axis=1, inplace=True)

df['birth'] = pd.to_datetime(df[['year', 'month', 'day']], format='%y%m%d')

df['birth_day'] = pd.to_datetime(dict(year=df['year'], month=df['month'], day=df['day']),format='%Y-%m-%d')