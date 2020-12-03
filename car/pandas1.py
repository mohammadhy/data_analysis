import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score



df = pd.read_csv('data.csv',error_bad_lines=False)



#print(df.head())

#print(df.columns)

#print(df[['Number of Doors', 'Engine HP','Engine Cylinders' ]][10:25])

##2:index
#print(df.iloc[2])

#print(df.describe())

## 0:row 1:column
#print(df.iloc[0,1])

##Write Filter:
#print(df.loc[(df['Engine HP'] > 400) & (df['Market Category'] == 'Luxury') & (df['Year'] > 2015)])

##choose multi culomns in diffrent dataset:
i_dont_now = df[['highway MPG' ,'city mpg' , 'Popularity','MSRP']]

##delete by index culomns: 
df.drop(df.columns[[12, 13, 14, 15]],axis=1 ,inplace = True) 



##rearange the columns:
df1 = df[['Vehicle Style', 'Market Category', 'Number of Doors', 'Engine Cylinders', 
         'Engine HP', 'Make', 'Model', 'Year', 'Vehicle Size', 'Driven_Wheels', 'Engine Fuel Type', 'Transmission Type']]


##change to lowercase value of columns:
df1['Vehicle Style'] = df1['Vehicle Style'].str.lower()
##chnge value to list of value:
data = df['Vehicle Style'].values.tolist()
##change to have same datatype:
#df1['Market Category'] = df1['Market Category'].astype(str)
'''
plt.hist(df1['Engine HP'])
plt.hist(df1['Engine Cylinders'])
plt.legend(loc="upper left")
plt.ylabel('per house')
plt.xlabel('hp')
'''
df1.isnull().sum()
df1.dropna(inplace=True)
df1.isnull().sum()

#sns.boxplot(x ='Number of Doors', y ='Engine Cylinders', data = df1)


door = pd.get_dummies(df1['Number of Doors'],drop_first=True)

df1 = pd.concat([df1,door], axis = 1)

df1.drop(['Vehicle Style', 'Market Category', 'Make','Model', 'Year','Vehicle Size', 'Driven_Wheels', 'Engine Fuel Type', 'Transmission Type'], axis=1, inplace=True)

x = df1.drop(['Engine HP'], axis=1)

y = df1['Engine HP']

x_train, x_test, y_train, y_test = train_test_split(x ,y, test_size=0.3, random_state=1)

model = LogisticRegression()

model.fit(x_train, y_train)

predict = model.predict(x_test)

classification_report(y_test, predict)

print(accuracy_score(y_test, predict) * 100)

confusion_matrix(y_test, predict)

