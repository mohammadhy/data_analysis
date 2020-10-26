#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:33:31 2020

@author: hassan
"""
import pandas as pd
uname = ['user_id', 'gender', 'age', 'occupation', 'zip']
user = pd.read_table('/home/hassan/python_code/pandas/pydata-book-2nd-edition/datasets/movielens/users.dat',
                     sep='::', header=None, names=uname)
rname = ['user_id', 'movie_id', 'rating', 'timestamp']
rating =pd.read_table('/home/hassan/python_code/pandas/pydata-book-2nd-edition/datasets/movielens/ratings.dat',
                     sep='::', header=None, names=rname)

mname = ['movie_id', 'title', 'genres']
movie = pd.read_table('/home/hassan/python_code/pandas/pydata-book-2nd-edition/datasets/movielens/movies.dat',
                     sep='::', header=None, names=mname)

data = pd.merge(pd.merge(user, rating), movie)

mean_rating = data.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')

rate_by_title = data.groupby('title').size()

active = rate_by_title.index[rate_by_title >= 250]

mean_rating = mean_rating.loc[active]

top_m = mean_rating.sort_values(by='M', ascending=False)

mean_rating['differ'] = mean_rating['F'] - mean_rating['M']

sort_by_differ = mean_rating.sort_values(by='differ')



