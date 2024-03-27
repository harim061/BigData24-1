# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:29:52 2024

@author: doris
"""
import pandas as pd
import csv
#다음 SQL 질의에 해당되는 python 문장을 작성하여보아라.
#[Sample CSV 파일] – emp.csv
#[질의 3-1] emp.csv를 읽어서 DataFrame emp 만들기
df = pd.read_csv('emp.csv')

#[질의 3-2] SELECT * FROM Emp;
df

#[질의 3-3] SELECT ename FROM Emp;
df['ENAME']
df.ENAME
df.loc[:,'ENAME']
df.iloc[:,1]

#[질의 3-4] SELECT ename, sal FROM Emp;
df[['ENAME','SAL']]

#[질의 3-5] SELECT DISTINCT job FROM Emp;

unique_jobs_df = pd.DataFrame(df['JOB'].unique(), columns=['JOB'])
unique_jobs_df


#[질의 3-6] SELECT * FROM Emp WHERE sal < 2000;
cond=df.SAL<2000
df[cond]


df[df.SAL<2000]

#[질의 3-7] SELECT * FROM Emp WHERE sal BETWEEN 1000 AND 2000;
cond = (df.SAL <= 1500) &( df.JOB =='SALESMAN')
df[cond]

#[질의 3-8] SELECT * FROM Emp WHERE sal >= 1500 AND job= ‘SALESMAN’;
cond = (df.SAL >= 1500) & (df.JOB =='SALESMAN')
df[cond]

#[질의 3-9] SELECT * FROM Emp WHERE job IN ('MANAGER', 'CLERK');
cond = df.JOB.isin(['MANAGER', 'CLERK'])
df[cond]

#[질의 3-10] SELECT * FROM Emp WHERE job NOT IN ('MANAGER', 'CLERK');
cond = ~df.JOB.isin(['MANAGER', 'CLERK'])
df[cond]

#[질의 3-11] SELECT ename, job FROM Emp WHERE ename LIKE 'BLAKE';
cond = df.ENAME == 'BLAKE'
df[cond][['ENAME','JOB']]

#[질의 3-12] SELECT ename, job FROM Emp WHERE name LIKE '%AR%';
cond = df.ENAME.str.contains('AR')
df[cond][['ENAME','JOB']]

#[질의 3-13] SELECT * FROM Emp WHERE ename LIKE '%AR%' AND sal >= 2000;
cond = (df['ENAME'].str.contains('AR')) & (df['SAL'] >= 2000)
df[cond]

#[질의 3-14] SELECT * FROM Emp ORDER BY ename;
df.sort_values(by = 'ENAME')

#[질의 3-15] SELECT SUM(sal) FROM Emp;
df['SAL'].sum()

#[질의 3-16] SELECT SUM(sal) FROM Emp WHERE job LIKE 'SALESMAN';
cond = df.JOB == 'SALESMAN'
df[cond]['SAL'].sum()

#[질의 3-17] SELECT SUM(sal), AVG(sal), MIN(sal), MAX(sal) FROM Emp;
df['SAL'].agg(['sum', 'mean', 'min', 'max'])

#[질의 3-18] SELECT COUNT(*) FROM Emp;
df.shape[0]

#[질의 3-19] SELECT COUNT(*), SUM(sal) FROM Emp GROUP BY job;
df.groupby('JOB').agg({'SAL':['count','sum']})

#[질의 3-20] SELECT * FROM Emp WHERE comm IS NOT NULL;
cond = ~df['COMM'].isnull()
df[cond]


