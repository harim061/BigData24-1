# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:37:38 2024

@author: doris
"""

import warnings
warnings.filterwarnings(action='ignore') 

# ### - 머신러닝 패키지 sklearn 설치

# ## 1) 데이터 수집
# In[1]:
import numpy as np
import pandas as pd

from sklearn.datasets import fetch_openml
boston = fetch_openml(name='boston')

X:{ 59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70}
Y:{ 209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204}

# In[3]:
boston_df = pd.DataFrame(boston.data, columns = boston.feature_names)
boston_df.head()

# In[4]:
boston_df['PRICE'] = boston.target
boston_df.head()
boston_df.to_csv("./DATA/BostonHousing.csv", index=False)
# In[6]:
print('보스톤 주택 가격 데이터셋 크기 : ', boston_df.shape)

# In[7]:
boston_df.info()
boston_df['CHAS']=boston_df['CHAS'].astype('int')
boston_df['RAD']=boston_df['RAD'].astype('int')
# ## 3) 분석 모델 구축
# In[8]:
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# In[10]:
# X, Y 분할하기
Y = boston_df['PRICE']
X = boston_df.drop(['PRICE'], axis=1, inplace=False)