#python3.7
"""
Wed Nov 4 09:55:51 2020

@author: HY
"""
#1: import library which we need it 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2:load dataset StudentsPerformance.csv:
data = pd.read_csv('/home/hassan/python_code/pandas/StudentsPerformance.csv')

#3:look at data and detect na value and type of column and prepare data to visualize:
print(data.info()) #1000:rows 8:columns

#3.1: creat new column and put result of sum of math score reading score writing score:
data['score'] = data['math score'] + data['reading score'] + data['writing score']

#3.2: delete math score reading score writing score:
data.drop(columns=['math score', 'reading score', 'writing score'],inplace=True)

#3.3: how many m and f participate in exam:
how_f_m = data.groupby('gender')['score'].count()
plt.bar(how_f_m.index, how_f_m.values)
plt.show()
#3.4: detect minimum score :
min_f_m = data.groupby('gender')['score'].min()
plt.bar(min_f_m.index, min_f_m.values)
plt.show()

#3.5: how many students in each group:
each_group = data.groupby('race/ethnicity')['gender'].size()
plt.bar(each_group.index, each_group.values)
plt.show()

#3.6: how many f and m in each group[A, B, C, D, E]:
'''
we have 2 method for do this 
(1) : use pivot table with use race/ethnicity as index and column must be gender
(2) : use groupby g = data.groupby('race/ethnicity').gender
                  g.value_counts() 
'''
f_m_eachgroup = data.pivot_table('lunch',index='race/ethnicity', columns=['gender'], aggfunc='count')
f_m_eachgroup.plot(title='each f and m in which group',ylabel='count')

#3.7 : degree on different level:
degree = data.groupby('parental level of education').gender.count()
plt.barh(degree.index, degree.values)

#3.8 : how many f and m in degree:
f_m_degreegroup = data.pivot_table('lunch',index='parental level of education', columns=['gender'], aggfunc='count')
f_m_degreegroup.plot(kind='barh')











