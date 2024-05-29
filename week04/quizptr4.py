# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:06:48 2024

@author: doris
"""
import csv 

f = open('202402.csv')
f2 = open('201402.csv')

data = csv.reader(f,delimiter=',')
data2 = csv.reader(f2,delimiter=',')

next(data)
next(data2)

result24=[]
result14=[]
result = []

for row in data:
    for row2 in data2:
        if (row[0] == row2[0]):
            result.append(int(row2[1].replace(',','')) - int(row[1].replace(',','')))
        break
    
print(result)
    
#%%

import matplotlib.pyplot as plt
plt.bar(range(16),result)
plt.show()

#%%

import pandas as pd

pd24 = pd.read_csv('202402.csv',encoding='cp949',delimiter=',')
pd14 = pd.read_csv('201402.csv',encoding='cp949',delimiter=',')

pop24 = pd24['2024년02월_총인구수']
pop14 = pd14['2014년02월_총인구수']
result2 = []

for i in range(len(pop24)):
    result2.append(int(pop14[i].replace(',',''))-int(pop24[i].replace(',','')))

print(result2)    

#%%

plt.bar(range(18),result)
plt.show()