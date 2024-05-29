# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:12:57 2024

@author: doris
"""

import numpy as np
import pandas as pd

df = pd.DataFrame([[89.2,92.5,'B'],
                   [90.8,92.8,'A'],
                   [89.9,95.2,'A'],
                   [89.9,95.2,'C'],
                   [89.9,90.2,'B']],
              columns = ['중간고사','기말고사','성적'],
              index = ['1반','2반','3반','4반','5반'])


df['중간고사']['1반']
df['중간고사'][0]
type(df)

df['중간고사']
type(df['중간고사'])
df['중간고사'][0:2]
type(df['중간고사'][0])
type(df['중간고사'][0:2])
df['중간고사']['1반':'2반']
type(df['중간고사']['1반':'2반'])

df.loc['1반']
type(df.loc['1반'])
df.loc[:,'중간고사']
type(df.loc[:,'중간고사'])
df.loc['1반':'2반']['중간고사']
df.loc['1반','중간고사']
type(df.loc['1반':'2반']['중간고사'])
df.loc['1반'][0]

df.iloc[0]
type(df.iloc[0])
df.iloc[0]['중간고사']
type(df.iloc[0]['중간고사'])

df.loc[df.성적 == 'B']
x = df[df.성적 =='B']
df.loc[(df.성적 =='A') & (df.중간고사 >= 90)]
df.loc[df.성적.isin(['B','C'])]


cond=df.성적 == 'B'
df[cond]

df.성적 =='B'
df['성적'] =='B'

df.loc[(df.성적 =='A')&(df.중간고사 >= 90)]

cond1 = (df.성적 =='A')
cond2 = (df.중간고사 >= 90)
df[cond1 & cond2]

df.loc[df.성적.isin(['B','C'])]

df.describe();
df.info()

df.중간고사.describe()
df.head(1)
df.중간고사.unique()
df.중간고사.mean()
df.describe().loc['mean','중간고사']
df.중간고사.value_counts()
df_mean = df.중간고사.mean()
df.중간고사.map(lambda p: p - df_mean)

df.groupby('중간고사').중간고사.count()
df.groupby('중간고사').중간고사.min()
df.groupby('중간고사').중간고사.agg([len,min,max])
df.sort_values(by='중간고사')
df.sort_values(by='중간고사',ascending=False)
df.sort_index(ascending=False)


g1=df.groupby('성적')
g2=df.groupby('성적').count()
g3=df.groupby('성적').sum()

# select 중간고사,count(*) from df group by 기말고사;

df.loc['6반'] = [10,10,np.nan]
df[pd.isnull(df.성적)]
df.isnull()

df.rename(columns={'등급':'등급2'},inplace=True)
df.rename_axis('반이름',axis='rows')

df0 = pd.concat([df])
