# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:18:36 2024

@author: doris
"""

# 10.1
import numpy as np

# 혼동 행렬 값
TP = 100
TN = 50
FP = 10
FN = 5

# 총 환자 수
n = 165

# Accuracy 계산
accuracy = (TP + TN) / n

# Recall 계산
recall = TP / (TP + FN)

# Fall-out 계산
fall_out = FP / (FP + TN)

# Specificity 계산
specificity = TN / (TN + FP)

# Precision 계산
precision = TP / (TP + FP)

# F1 Score 계산
f1_score = 2 * (precision * recall) / (precision + recall)

# 결과 출력
print(f'Accuracy: {accuracy:.4f}')
print(f'Recall: {recall:.4f}')
print(f'Fall-out: {fall_out:.4f}')
print(f'Specificity: {specificity:.4f}')
print(f'Precision: {precision:.4f}')
print(f'F1 Score: {f1_score:.4f}')


# Q10.2

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, roc_auc_score

# 유방암 데이터셋 로드
b_cancer = load_breast_cancer()

# 데이터 프레임 생성
b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target

# 데이터 스케일링
scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)

# X, Y 설정
Y = b_cancer_df['diagnosis']
X = b_cancer_scaled

# 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# 로지스틱 회귀 모델 훈련
lr_b_cancer = LogisticRegression()
lr_b_cancer.fit(X_train, Y_train)

# 예측
Y_predict = lr_b_cancer.predict(X_test)

# 성능 지표 계산
confusion = confusion_matrix(Y_test, Y_predict)
accuracy = accuracy_score(Y_test, Y_predict)
precision = precision_score(Y_test, Y_predict)
roc_auc = roc_auc_score(Y_test, lr_b_cancer.predict_proba(X_test)[:, 1])

# 결과 출력
print(f'Confusion Matrix:\n{confusion}')
print(f'Accuracy: {accuracy:.3f}')
print(f'Precision: {precision:.3f}')
print(f'ROC_AUC: {roc_auc:.3f}')

