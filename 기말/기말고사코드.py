#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
X_train = pd.read_csv("XX_train.csv")
Y_train = pd.read_csv("YY_train.csv")
X_train.info()
X_train.head().T

# train-test 검증 데이터 분리 20%


# 분석에 필요하지 않은 컬럼 제거
ID = X_train.pop('ID')


# 라벨 인코딩 - 명목형 변수 / LabelEncoding(), get_dummies()


# minmaxscalings

# 모델 생성1(RandomForest)

# # 모델 성능 평가
from sklearn.metrics import roc_auc_score
pred1=model1.predict(x_test)
print('RF',roc_auc_score(y_test, pred1)) # 

