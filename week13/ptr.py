# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:07:17 2024

@author: doris
"""

import csv

f = open('seoul.csv','r',encoding='cp949')
data = csv.reader(f,delimiter=',')
print(data)
f.close()

#%%

f = open('seoul.csv',encoding='cp949')
data = csv.reader(f)
for row in data:
    print(row)
    
f.close()

#%%  헤더 저장하기

f=open('seoul.csv')
data =csv.reader(f)
header = next(data)
print(header)
f.close()

#%%
import csv
f =open('seoul.csv')
data=csv.reader(f)
header = next(data)

for row in data:
    print(row)

f.close()

#%% 서울의 최고 기온
# data 한 행씩 출력하기
import csv
f = open('seoul.csv')
data =csv.reader(f)

header = next(data)

for row in data:
    print(row)


f.close()

#%%
#최고 기온을 실수로 변환하여 한 행씩 출력하기

f = open('seoul.csv')
data = csv.reader(f)
header = next(data)

for row in data:
    if row[4] != '':
        row[4] = float(row[4]) 
    print(row)
    
f.close()

#%% 최고 기온 최고 기온이었던 날짜 찾기

f =open('seoul.csv')
data = csv.reader(f)
header =next(data)
max_t = -999
max_d = ''

for row in data:
    if row[-1] == '':
        row[-1] = -999
    
    else:
        row[-1] = float(row[-1])
        
    if (row[-1] > max_t):
        max_t = row[-1]
        max_d = row[0]
            

print(max_t)
print(max_d)
f.close()

#%% matplotlib

import matplotlib.pyplot as plt

plt.plot([10,20,30,40])
plt.show()

#%%

plt.plot([1,2,3,4],[12,43,25,15])
plt.show()

#%%
plt.plot([10,20,30,40],label='asc')
plt.plot([40,30,20,10],label='desc')
plt.title('plotting')
plt.legend()
plt.show()  

#%%
plt.plot([10,20,30,40],label='pink',color='pink')
plt.plot([40,30,20,10],label='blue',color='blue')
plt.title('plotting')
plt.legend()
plt.show()  

#%%
plt.plot([10,20,30,40], 'r.',label='circle')
plt.plot([40,30,20,10],'b^',label='triangle up')
plt.title('plotting')
plt.legend()
plt.show()  

#%%
import csv
f = open('seoul.csv')
data = csv.reader(f)
result = []
next(data)
for row in data:
    
    if row[-1] != '':
        if row[0].split('-')[1] == '06' and row[0].split('-')[2]=='01':
            result.append(float(row[-1]))

print(result)

f = open('seoul.csv')
data = csv.reader(f)
result2 = []

next(data)
for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '01' and row[0].split('-')[2]=='01':
            result2.append(float(row[-1]))

print(result2)


#%%
import matplotlib.pyplot as plt
plt.rc('font',family ='Malgun Gothic')
plt.title('내 생일 ')
plt.rcParams['axes.unicode_minus'] = False
plt.plot(result,'r')
plt.plot(result2,'b')
plt.show()

#%%
s = 'hello python'
print(s.split())

date = '1907-10-01'
print(date.split('-'))

print(date.split('-')[0])
print(date.split('-')[1])
print(date.split('-')[2])


#%%

plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()

#%%
import random

dice = []
for i in range(5):
    dice.append(random.randint(1,6))
    
print(dice)

plt.hist(dice,bins=6)
plt.show()

#%%

f = open('seoul.csv')
data= csv.reader(f)
next(data)
result = []
result_j = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            result.append(float(row[-1]))
        if row[0].split('-')[1] == '01':
            result_j.append(float(row[-1]))
        
plt.hist(result,bins=100,color='r')
plt.hist(result_j,bins=100, color='b')
plt.show()

#%%
plt.boxplot([result,result_j])
plt.show()

#%%
f = open('seoul.csv')
data= csv.reader(f)
next(data)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data:
    if row[-1] != '':
        
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))
        
plt.boxplot(month)
plt.show()

#%%
print('신도림' in '서울시 신도림동')

#%%
f = open('age.csv')
data = csv.reader(f)
result = []

for row in data:
    if '아름동' in row[0]:
        for i in row[3:]:
            result.append(int(i))
            
print(result)

#%%
plt.bar(range(101),result)
plt.show()

#%%
plt.barh(range(101),result)
plt.show()

#%%
plt.style.use('ggplot')
plt.plot(result)
plt.show()

#%%
plt.bar(range(6),[1,2,3,5,6,7])
plt.show()

#%%
f = open('gender.csv')
data = csv.reader(f)
m =  []
f = []

for row in data:
    if '신림동' in row[0]:
        for i in range(0,101):
            m.append(int(row[i+3]))
            f.append(int(row[i-101]))
#%%
f = open('gender.csv')
data = csv.reader(f)
m =  []
f = []

for row in data:
    if '신림동' in row[0]:
        for i in row[3:104]:
            m.append(-int(i))
            
        for i in row[106:]:
            f.append(int(i))

#%%
plt.rc('font',family='Malgun Gothic')
plt.title("신도림")
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label ='여성')
plt.legend()

plt.show()


# In[]:
size=[2441,2312,1031,1233]
plt.axis('equal')
plt.pie(size)
plt.show()
    
#%%

label = ['a','b','c','d']
plt.axis('equal')
color = ['darkmagenta','deeppink','blue','red']
plt.pie(size,labels=label,autopct="%.1f%%",colors=color,explode=(0,0,0.1,0))
plt.legend()
plt.show()

#%%

f =open('gender.csv')
data = csv.reader(f)

size = []

name= input("지역 이름?")
for row in data:
    if( name in row[0]):
        m = 0
        f = 0
        
        for i in range(101):
            m += int(row[i+3])
            f += int(row[i+106])
    
        break
    
size.append(m)
size.append(f)
print(size)

#%%
color = ['crimson','darkcyan']
plt.axis('equal')
plt.pie(size, labels=['남','여'],autopct = '$.1f%%',colors=color,startangle = 90)
plt.title('제주도')
plt.show()

#%%
f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('어느 동네?')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i + 103]))
            
        break
#%%
plt.plot(m , label ='Male')
plt.plot(f, label='female')
plt.legend()
plt.show()

#%%
f = open('gender.csv')
data = csv.reader(f)

result = []

name = input('어느 동네?')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            result.append(int(row[i])- int(row[i+103]))
            
        break
    
    
#%%
plt.bar(range(101),result)
plt.show()

#%%
plt.scatter([1,2,3,4],[10,30,20,40], s= [100,200,250,300], c=range(4), cmap='jet')
plt.colorbar()
plt.show()

#%%
x = []
y = []

size = []

for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))

plt.scatter(x,y,size,c=size,cmap='jet',alpha=0.7)
plt.colorbar()
plt.show()

#%%
plt.scatter(m,f,cmap='jet',alpha=0.6)
plt.colorbar()
plt.plot(range(max(m)),range(max(m)),'g')
plt.show()

#%%
import math

f = open('gender.csv')
data = csv.reader(f)

m = []
f = []
size = []

name = input('어느 동네?')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i + 103]))
            size.append(math.sqrt(int(row[i])+int(row[i+103])))
            
        break

#%%
plt.figure(figsize=(10,5),dpi=300)
plt.title(name +"지역 인구")
plt.scatter(m,f,size,cmap='jet', c=range(101),alpha =0.5)
plt.colorbar()
plt.plot(range(max(m)),range(max(m)),'g')
plt.xlabel('남성 인구')
plt.ylabel('여성 인구')
plt.show()