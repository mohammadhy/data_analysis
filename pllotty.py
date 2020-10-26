import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv('/home/hassan/python_code/pandas/StudentsPerformance.csv')


gen = pd.get_dummies(data['gender'], drop_first=True)
group = pd.get_dummies(data['race/ethnicity'])
degree = pd.get_dummies(data['parental level of education'])
data = pd.concat([data, gen, group, degree], axis=1)
data['score'] = data['math score'] + data['reading score'] + data['writing score']
data.drop(['gender', 'race/ethnicity','parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score' ], axis=1, inplace=True)

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

date = pd.date_range('1/1/2000', periods=400)
date = pd.DataFrame(date)
date.rename(columns={0:'year'}, inplace=True)

df = pd.read_csv('/home/hassan/python_code/pandas/age_salary.csv')
df = df.drop(['Gender'], axis=1)
df = pd.concat([df, date], axis=1)
df.drop(df.index[400:])

result =  pd.merge(df, data, left_index=True, right_index=True)

'''
exyear = result['User ID'].values
password = [str(k)[-4:] for k in exyear]
password = pd.DataFrame(password)
password.rename(columns={0:'password'}, inplace=True)
'''


grouped = result.groupby('year')['EstimatedSalary','score']
grouped.agg(['min', 'max'])


#for visualiziation:
    
ticks = ax1.set_yticks([20, 25, 30, 40, 50, 60])
ax1.set_title('this is for age')
ax1.set_ylabel('AGE')
a = df.iloc[:100, 1]
#a= pd.DataFrame(a)
ax1.plot(a)


ax2.set_title('this is for sex')
ticks2 = ax2.set_yticks([0,1])
label2 = ax2.set_yticklabels(['men', 'women'])
ax2.set_ylabel('GENDER')
ax2.plot(result.loc[:100, 'male'], 'g*')


fig, axes = plt.subplots(2, 1)
d = result.loc[:10, 'Age']
d.plot.bar(ax=axes[0], color='g', alpha=0.9)
d.plot.barh(ax=axes[1], color='b', alpha=0.5)


fig, axes = plt.subplots(2, 1, figsize=(10, 8))
fig.text(0.05, 0.5, 'counter ', ha='center', va='center', rotation='vertical')
pg = result.groupby(['Age', 'Purchased']).size().unstack()
pg[0].plot(kind='bar', rot=0, ax=axes[0], title='not buy')
pg[1].plot(kind='bar', rot=0, ax=axes[1], title='buy')

mean_age = result.pivot_table(values='Age', index='male', columns='score', aggfunc='mean')
mean_age = mean_age.stack().reset_index()
mean_age.sort_values(by=0, inplace=True)
mean_age_s = mean_age[:30]
sns.barplot(x=0, y='score', hue='male', data=mean_age_s)

