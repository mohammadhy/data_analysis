#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:42:03 2020

@author: hassan
"""
import pandas as pd
import json
import seaborn as sns
import numpy as np

path = '/home/hassan/python_code/pandas/pydata-book-2nd-edition/datasets/bitly_usagov/example.txt'
record = [json.loads(line) for line in open(path)]

time = [rec['tz']for rec in record if 'tz' in rec]
data = pd.DataFrame(record)
tz_counts = data['tz'].value_counts()
clean_tz = data['tz'].fillna('Missing')

clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()

subset = tz_counts[:10]
#sns.barplot(y=subset.index, x = subset.values)
result = pd.Series([x.split()[0] for x in data.a.dropna()])
print(result.value_counts())

cdata = data[data.a.notnull()]
cdata['os'] = np.where(cdata['a'].str.contains('Windows'),'windows', 'not_windows')

gp_tz_os = cdata.groupby(['tz', 'os'])
agg_gto = gp_tz_os.size().unstack().fillna(0)

indexer = agg_gto.sum(1).argsort()
count_subset = agg_gto.take(indexer[-10:])

count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
#sns.barplot(x='total', y='tz', hue='os', data=count_subset)

def normalize(group):
    group['normalize'] = group.total / group.total.sum()
    return group
result = count_subset.groupby('tz').apply(normalize) 
sns.barplot(x='normalize', y='tz', hue='os', data=result)

