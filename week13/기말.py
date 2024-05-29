# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:49:18 2024

@author: doris
"""

import pandas as pd
import numpy as np
X_train = pd.read_csv()
Y_train = pd.read_csv()

# train text 분리
# 컬럼 제거
# 라벨 인코딩 
# minmaxscaling
# 모델 성능 randomforest

# 모델 성능 평가
from sklearn.metrics import roc_auc_score
pred1 = model1.predict(x_train)
print('RF',roc_auc_score(y_test, pred1))