#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:32:06 2020

@author: hassan
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

#salary = pd.read_csv('/home/hassan/python_code/pandas/Salary.csv')
#job = pd.read_csv('/home/hassan/python_code/pandas/job_skills.csv')
male = pd.read_csv('/home/hassan/python_code/pandas/age_salary.csv')
youtube = pd.read_csv('/home/hassan/python_code/pandas/USvideos.csv')
male = male['Gender']
male = pd.DataFrame(male)
youtube.drop(columns=['description', 'video_error_or_removed',
                      'ratings_disabled', 'thumbnail_link',
                      'comments_disabled', 'channel_title', 'tags', 'video_id', 'category_id'], inplace=True)
#we add male columns from another datasets to analysis the male and femele like which title more
youtube = youtube[:400].join(male)

pivot_df_like = youtube.pivot_table('likes', index='title', columns='Gender', aggfunc='mean')
pivot_df_dislike = youtube.pivot_table('dislikes', index='title', columns='Gender', aggfunc='mean')

top_male_like = pivot_df_like.sort_values(by='Male', ascending=False)

pivot_df_like['diff'] = pivot_df_like['Female'] - pivot_df_like['Male']

diff_like = pivot_df_like.sort_values(by='diff', ascending=False)


format_time = []
for t in youtube['publish_time']:
    new_date = t.split('T')[1]
    new_date = new_date.split('.')[0]
    format_time.append(new_date)
format_time = pd.DataFrame(format_time)

youtube = youtube.join(format_time)

youtube.drop(columns=['publish_time'], inplace=True)
youtube.rename(columns={0:'date'}, inplace=True)
'''
che time bishtarin like kardan marda ya zana
'''
pivot_like = youtube.pivot_table(values='likes', index='date', columns='Gender', fill_value=0.0)
pivot_like.plot(title='what time people most like video:')

'''
2 nafar az women k bishtarin view kardan va moghayese ba men:
'''

who_see = youtube.pivot_table('views', index='title', columns='Gender')
who_see = who_see.sort_values(by='Female', ascending=False)
who_see = who_see.iloc[0:2,:]
fig, axes = plt.subplots(2, 1, figsize=(10,8))
who_see['Female'].plot(kind='bar', rot=0, ax=axes[0], title='women')
who_see['Male'].plot(kind='bar', rot=0, ax=axes[1], title='men')

