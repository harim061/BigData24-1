# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:24:20 2024

@author: doris
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report, accuracy_score
import graphviz

# 데이터 로드
data = pd.read_csv('playtennis.csv')

data = pd.get_dummies(data)

# 특성과 레이블 분리
X = data.drop('PlayTennis', axis=1)
y = data['PlayTennis']

# 훈련 및 테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 의사결정 트리 모델 생성 및 훈련
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

# 예측
y_pred = dt_classifier.predict(X_test)

# 성능 지표 출력
print(classification_report(y_test, y_pred))

# 정확도 출력
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# 트리 시각화
dot_data = export_graphviz(dt_classifier, out_file=None, 
                           feature_names=X.columns,  
                           class_names=dt_classifier.classes_,  
                           filled=True, rounded=True,  
                           special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("Decision_Tree")