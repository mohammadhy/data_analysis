#python3.8.5
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
plt.figure()
#3.4: detect minimum score :
min_f_m = data.groupby('gender')['score'].min()
plt.bar(min_f_m.index, min_f_m.values)
plt.show()
plt.figure()
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
plt.figure()
f_m_eachgroup = data.pivot_table('lunch',index='race/ethnicity', columns=['gender'], aggfunc='count')
f_m_eachgroup.plot(title='each f and m in which group',ylabel='count')
plt.Figure()
#3.7 : degree on different level:
degree = data.groupby('parental level of education').gender.count()
plt.barh(degree.index, degree.values)
plt.figure()
#3.8 : how many f and m in degree:
f_m_degreegroup = data.pivot_table('lunch',index='parental level of education', columns=['gender'], aggfunc='count')
f_m_degreegroup.plot(kind='barh')

plt.figure()
plt.pie(how_f_m,labels=['male','female'] ,explode=(0.1, 0), shadow=True,autopct='%1.1f%%')


def group_(tt):
    if tt in ['group A']:
        return 0
    elif tt in ['group B']:
        return 1
    elif tt in ['group C']:
        return 2
    elif tt in ['group D']:
        return 3
    elif tt in ['group E']:
        return 4
df = data.copy()

df['race/ethnicity'] = df['race/ethnicity'].transform(group_)

df['gender'] = pd.get_dummies(df['gender'])



def level_edu(columns):
    if columns in ["associate's degree"]:
        return 0
    elif columns in ["bachelor's degree"]:
        return 1
    elif columns in ["master's degree"]:
        return 2
    elif columns in ["some college"]:
        return 3
    elif columns in ["high school"]:
        return 4
    elif columns in ["some high school"]:
        return 5
df['parental level of education'] = df['parental level of education'].map(level_edu)
        
df['lunch'] = pd.get_dummies(df['lunch'])

df.drop('test preparation course', inplace=True, axis='columns')


def classi(x):
    if x <= np.quantile(df['score'], 0.25):
        return 2
    elif x > np.quantile(df['score'], 0.25) and x <= np.quantile(df['score'], 0.50):
        return 1
    elif x >= np.quantile(df['score'], 0.5):
        return 0
df['class'] = df['score'].apply(classi)


from sklearn.model_selection  import  train_test_split, cross_val_predict
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

x = df.iloc[:, :-1]
y = df.iloc[:, -1]
    
''' run on commandline ==> dot -Tpng moon_tree.dot -o moon_tree.png '''



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

tree_student = DecisionTreeClassifier(max_depth=5)
tree_student.fit(x_train, y_train)
y_predict = tree_student.predict(x_test)

export_graphviz( 

        tree_student,
        feature_names=x.columns,
        out_file=('tree_student.dot'),
        rounded=True,
        filled=True)

from sklearn.metrics import  accuracy_score, confusion_matrix

print(confusion_matrix(y_test, y_predict))






'''
from matplotlib.colors import ListedColormap
def plot_decision_boundary(clf, X, y, axes=[0, 4, 0, 3],legend=False, plot_training=True):
    x1s = np.linspace(axes[0], axes[1], 200)
    x2s = np.linspace(axes[2], axes[3], 200)
    x1, x2 = np.meshgrid(x1s, x2s)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    y_pred = clf.predict(X_new).reshape(x1.shape)
    custom_cmap = ListedColormap(['#fafab0','#9898ff','#a0faa0'])
    plt.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)
    
    if plot_training:
        plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo", label="class_0")
        plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bs", label="class_1")
        plt.axis(axes)
    else:
        plt.xlabel(r"$x_1$", fontsize=18)
        plt.ylabel(r"$x_2$", fontsize=18, rotation=0)
    if legend:
        plt.legend(loc="lower right", fontsize=14)


plt.figure(figsize=(8, 4))
plot_decision_boundary(tree_student, x_train.iloc[:, :2], y, legend=False)
plt.plot([0, 3.5], [0.8, 0.8], "k:", linewidth=2)
plt.plot([0, 3.5], [2, 2], "k--", linewidth=2)
plt.text(1.0, 0.9, "Depth=0", fontsize=15)
plt.text(1.0, 2.40, "Depth=1", fontsize=13)

'''





