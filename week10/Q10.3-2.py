# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:47:36 2024

@author: doris
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report, accuracy_score
import graphviz

# 데이터 로드
data = {
    'Day': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'],
    'Outlook': ['Sunny', 'Overcast', 'Overcast', 'Rain', 'Sunny', 'Rain', 'Overcast'],
    'Temperature': ['Hot', 'Hot', 'Mild', 'Mild', 'Mild', 'Hot', 'Hot'],
    'Humidity': ['High', 'High', 'Normal', 'Normal', 'High', 'High', 'Normal'],
    'PlayTennis': ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
}
data = pd.DataFrame(data)

# 데이터 전처리: 문자열 데이터를 숫자형 더미 변수로 변환 (원핫 인코딩)
data = pd.get_dummies(data)

# 특성과 레이블 분리
X = data.drop('PlayTennis_Yes', axis=1)  # 'PlayTennis_Yes' 열을 특성에서 제외
y = data['PlayTennis_Yes']  # 'PlayTennis_Yes' 열을 레이블로 사용

# 의사결정 트리 모델 생성 및 훈련
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X, y)

# 예측
y_pred = dt_classifier.predict(X)

# 성능 지표 출력
print(classification_report(y, y_pred))

# 정확도 출력
accuracy = accuracy_score(y, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# 트리 시각화
dot_data = export_graphviz(dt_classifier, out_file=None, 
                           feature_names=X.columns,  
                           class_names=['No', 'Yes'],  
                           filled=True, rounded=True,  
                           special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("Decision_Tree")
