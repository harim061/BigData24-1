# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:31:33 2024

@author: doris
"""
import pandas as pd
import numpy as np

data ={
       'apples':[3,2,0,1],
       'oranges':[0,3,7,2]
       }


purchase = pd.DataFrame(data)
purchase


purchases = pd.DataFrame(data,index = ['June','Robert','Lily','David'])
purchases

col1 = pd.Series([3,2,0,1],name = 'apples')
col1

col2 = pd.Series([3,2,0,1],name = 'oranges', index=['June','Robert','Lily','David'])
col2

col1.name

col1.values
col1.index

purchase2 = pd.DataFrame(col1)
purchase2

purchase3 = pd.DataFrame(col2)
purchase3


col2 = pd.Series([3,2,0,1],name='oranges')
col2
purchase4 = pd.concat([col1,col2],axis = 1)
purchase4

purchase4.index = ['June','Robert','Lily','David']
purchase4

#purchase4.name
purchase4.index
purchase4.columns


data_dic = {
    'year':[2018,2019,2020],
    'sales':[350,480,1099]}

data_dic

df1 = pd.DataFrame(data_dic)
df1

data2 = ['1반','2반','3반','4반','5반']
df2 = pd.DataFrame([[89.2,92.5,90.8],[92.8,89.9,95.2]], index =['중간고사','기말고사'], columns=data2[0:3])
df2

data_df = [['20201101','홍','90','95'],['201111','김','93','94'],['222222','lee','87','97']]
df3 = pd.DataFrame(data_df)
df3

df3.columns=['학번','이름','중간','기말']
df3

df3.head(2)
df3.tail(2)

df3['이름']


import pandas as pd

df = pd.DataFrame([[60, 61,62],[70,71,72],[80,81,82],[90,91,92]],
                  index=['1반','2반','3반','4반'],columns = ['퀴즈1','퀴즈2','퀴즈3'])

df 
df.퀴즈1
df['퀴즈1']
df['퀴즈1'][2]

df.loc['2반']
df.loc['2반','퀴즈1']
df.loc['2반':'4반', '퀴즈1']
df.loc['2반':'4반','퀴즈1':'퀴즈3']

df.iloc[2]
df.iloc[2,1] # 80
df.iloc[2:4,0]
df.iloc[2:4, 0:2] #80 81 / 90 91
df.iloc[2:4, 0:1] #80 / 90


data2 = ['1반','2반','3반','4반','5반']
df = pd.DataFrame([[89.1,90.1,'B'],
                   [89.2,90.2,'A'],
                   [89.3,90.3,'A'],
                   [89.4,90.4,'C'],
                   [89.5,90.5,'B']],
                  index=data2, columns = ['중간','기말','성적'])

df

df['기말']
df.기말
df[['중간','기말']]
df['2반':'4반']
#df['2반','4반']
df['중간'][3]
df['중간']['1반':'2반']
df['중간'][0:2]
df[0:2]['중간']


df.loc['5반' ]
df.loc['1반':'2반','중간']
df.loc[:,'기말']

df.iloc[0:2]['중간']
df.iloc[4]


df[df['성적']=='B']
df[df.성적 =='B']

df[df.성적.isin(['B','C'])]

df.성적.isin(['B','C'])
df.loc[df.성적.isin(['B','C'])]

df[(df.성적 =='A') &( df.중간 >= 90)]
df.loc[(df.성적 =='A') &( df.중간 >= 90)]


df.describe()
df.중간.describe()

df.head(1)
df.중간.unique()
df.중간.mean()
df.중간.value_counts()
df_mean = df.중간.mean()
df.중간.map(lambda p  : p - df_mean)

df.groupby('중간').중간.count()
df.groupby('중간').중간.min()
df.groupby(['중간']).중간.agg([len,min,max])

df.sort_values(by='중간')
df.sort_values(by='중간', ascending=False)
df.sort_index(ascending=False)

df.dtypes
df.중간.dtypes
df.loc['6반'] = [10,10,np.nan]
df
df[pd.isnull(df.성적)]

df.rename(columns={'성적':'등급'})
df.rename_axis("반이름", axis='rows')


df1= pd.DataFrame([[89.1,90.1,'B'],
                   [89.2,90.2,'A'],
                   [89.3,90.3,'A'],
                   [89.4,90.4,'C'],
                   [89.5,90.5,'B']],
                  index=data2, columns = ['중간','기말','성적'])

df0 = pd.concat([df,df1])
df0

df4 = pd.read_csv('emp.csv')

df1.to_csv('./df1.csv',header =True)

len(df)
df.shape[0]
len(df.index)

df.shape[1]
len(df.columns)

df.count()
df.groupby('중간').size()

df.groupby('중간').count()

import matplotlib.pyplot as plt

x = [2016,2017,2018,2019,2020]
y = [350,410,520,695,543]

plt.plot(x,y)
plt.title('sales')
plt.xlabel('years')
plt.ylabel('sales')
plt.show()



y1 = [350,410,520,695]
y2 = [200,250,385,350]
x = range(len(y1))

plt.bar(x,y1,width = 0.7,color='blue')
plt.bar(x,y2,width = 0.7,color='red',bottom=y1)
plt.title('sales')
plt.xlabel('q')
plt.ylabel('sales')
xLabel = [1,2,3,4]

plt.xticks(x,xLabel,fontsize=10)
plt.legend(['chairs','desks'])
plt.show() 



