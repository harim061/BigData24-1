# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:40:06 2024

@author: doris
"""


import csv
with open('emp.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    data_list = list(reader)
print(data_list)

"""
import pandas as pd
dir(pd)
print(pd.read_csv.__doc__)
help(pd.read_csv)

dir(pd.DataFrame)
print(pd.DataFrame.dropna.__doc__)
help(pd.DataFrame.dropna)
"""


import pandas as pd
emp=pd.read_csv('emp.csv')
emp.head()
emp["ENAME"]
emp[emp["SAL"] >2000]