# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:59:36 2024

@author: doris
"""
# 데이터 처리
import csv
f = open('201402.csv', 'r', encoding='cp949') 
f2 = open('202402.csv','r',encoding='cp949')

population_number14 = {}
population_number24 = {}
population_change = {}

data  = csv.reader(f, delimiter=',')
data2 = csv.reader(f2,delimiter=',')
next(data)
next(data2)

#2014 읽기
for row in data :
    
    region_l = row[0].split('(')
    region = region_l[0]
    population = int(row[1].replace(',',''))
    
    population_number14[region] = population
    
f.close()

    
#2024 읽기
for row in data2:
    
    region_l = row[0].split('(')
    region = region_l[0]
    population = int(row[1].replace(',',''))
    
    population_number24[region] = population
    
f2.close()

    
#change 계산

for region, pop_2014 in population_number14.items():
    
    if region in population_number24:
        
        population_change[region] = population_number14[region] - population_number24[region]
  
for region, change in population_change.items():
    print(f'{region}: {change}')    


#bar 차트 그리기

import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False
plt.bar(population_change.keys(), population_change.values())

plt.title('Population Change from 2014 to 2024 by Region')
plt.xlabel('Region')
plt.ylabel('Population Change')
plt.xticks(rotation=45)
plt.savefig('population_change.png')
