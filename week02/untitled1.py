# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:23:02 2024

@author: doris
"""


import pandas as pd

data1 = [10,20,30,40, 50]
data1

data2 = ['1반','2반','3반','4반','5반']
data2

sr1 = pd.Series(data1)
sr1

sr2 = pd.Series(data2)
sr2

sr3 = pd.Series([101,102,103,104,105])
sr3

sr4 = pd.Series(['월','화','수','목','금'])
sr4

sr5 = pd.Series(data1, index=[1000,1001,1002,1003,1004])
sr5


sr6 = pd.Series(data1,index=data2)
sr6

sr7 = pd.Series(data2, index = data1)
sr7

sr8 = pd.Series(data2,index=sr4)
sr8

sr8[2]

sr8[-1]

sr8[0:4]

sr8.index

sr8.values


sr1 + sr3

sr4 + sr2

