# -*- coding: utf-8 -*-
"""
Created on Mon May 27 02:00:29 2024

@author: doris
"""

import pandas as pd

#3-1
data = pd.read_csv('emp.csv')

#3-2
data

#3-3
data['ENAME']

#3-4
data[['ENAME','SAL']]

#3-5
data.JOB.unique()

unique = pd.DataFrame(data.JOB.unique(),columns=['job'])
unique

#3-6
data[data['SAL']<2000]

#3-7
data[(data['SAL'] > 1000 )&( data['SAL'] < 2000)]

#3-8
data[(data['SAL']>=1500) & (data['JOB']=='SALESMAN')]

#3-9
data[data.JOB.isin(['MANAGER','CLERK'])]

#3-10
data[~data.JOB.isin(['MANAGER','CLERK'])]


#3-11
conf = data.ENAME=='BLAKE'
data[conf][['ENAME','JOB']]

#3-12
conf = data.ENAME.str.contains('AR')
data[conf][['ENAME','JOB']]


#3-13
cond = data.ENAME.str.contains('AR') & (data.SAL >= 2000)
data[cond]

#3-14
data.sort_values(by='ENAME')


#3-15
data.SAL.sum()

#3-16
cond = data.JOB ==  'SALESMAN'
data[cond].SAL.sum()

#3-17
data.SAL.agg(['sum','mean','min','max'])

#3-18
len(data.index)

#3-19
data.groupby('JOB').SAL.agg(['sum','count'])

#3-20
data[pd.isnull(data.COMM)]

#4-0
df = pd.read_csv('emp.csv')
df

#4-1
df['AGE'] = [30,40,50,30,40,50,30,40,50,30,40,50,30,40]
df

#4-2
df1 = pd.DataFrame([[9999,'ALLEN','SALESMAN']], columns=['EMPNO','ENAME','JOB'])
df = pd.concat([df,df1])
df


#4-3
cond =df['ENAME'] == 'ALLEN'
df = df.drop(df[cond].index)

#4-4
cond=df.HIREDATE
df = df.drop(columns='HIREDATE')


#4-5
cond = df.ENAME =='SCOTT'
df[cond].SAL = 3000
df

#5-1
df = df.rename(columns={'SAL':'OLDSAL'})

#5-2
df['NEWSAL'] = df['OLDSAL']
df

#5-3
df = df.drop(columns='OLDSAL')