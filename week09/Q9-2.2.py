# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:04:20 2024

@author: doris
"""

from sklearn import linear_model
from sklearn import datasets
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

# 데이터 로드
diabetes_data = datasets.load_diabetes()
X = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
y = diabetes_data.target

# 데이터 설명
num_features = X.shape[1]
num_samples = X.shape[0]
features = list(X.columns)

# Train/Test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 회귀분석 모델 생성 및 학습
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X_train, y_train)

# 예측 및 평가
prediction = linear_regression.predict(X_test)
r_squared = r2_score(y_test, prediction)
mean_squared_error_value = mean_squared_error(y_test, prediction)
rmse = mean_squared_error_value ** 0.5

# 결과 반환
(num_samples, features, r_squared, mean_squared_error_value, rmse)

print(r_squared)