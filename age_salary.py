# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:26:38 2020

@author: Asus
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import pandas as pd
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('age_salary.csv')

gender = pd.get_dummies(df['Gender'], drop_first=True)
df.drop('Gender', axis=1, inplace=True)
df = pd.concat([df,gender], axis = 1)
x = df.iloc[:, [2, 3, 5]].values
y = df.iloc[:, [4]].values

x_train, x_test, y_train, y_test = train_test_split(x ,y, test_size=0.3, random_state=1)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

model = LogisticRegression()

model.fit(x_train, y_train)
predict = model.predict(x_test)

print(accuracy_score(y_test, predict) * 100)

