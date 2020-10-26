
import pandas as pd 
import numpy as np

df_weather1 = pd.read_csv('weather.csv')
df_weather_melt = pd.melt(df_weather1, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')
df_weather = (df_weather_melt.pivot_table(index = ['year','month','day','id'], columns = 'element', values = 'temp')
       .reset_index().rename_axis(None, axis = 1))
#df_weather['date'] = pd.to_datetime(df_weather[['year', 'month', 'day']])

df_weather['day'] = df_weather['day'].str[1:3].astype(int)
df_weather['date'] = pd.to_datetime(df_weather[['year', 'month', 'day']], format='%Y%m%d')
df_weather.drop(columns=['year', 'month', 'day'], inplace=True)
