# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:58:42 2024

@author: doris
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# 데이터 정의
X = np.array([59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70]).reshape(-1, 1)
Y = np.array([209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204])

# 단일회귀분석 모델 생성 및 훈련
model = LinearRegression()
model.fit(X, Y)

# 회귀분석 계수 (α, β)
intercept = model.intercept_
slope = model.coef_[0]

# R_squared 값 구하기
r_squared = model.score(X, Y)

# X값이 58일 때 Y값 예측
predicted_y = model.predict(np.array([[58]]))

(intercept, slope, r_squared, predicted_y[0])