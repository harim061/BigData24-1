# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:28:52 2024

@author: doris
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
from IPython.display import Image
import pydotplus

# Iris 데이터 로드
iris = load_iris()
X = iris.data
y = iris.target

# 훈련 및 테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# n_estimators 값에 따른 정확도 조사
n_estimators_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
accuracies = []

for n_estimators in n_estimators_list:
    rfc = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    rfc.fit(X_train, y_train)
    accuracies.append(rfc.score(X_test, y_test))

# 정확도가 가장 높은 n_estimators 값 찾기
max_accuracy = max(accuracies)
best_n_estimators = n_estimators_list[accuracies.index(max_accuracy)]

print(f'가장 높은 정확도: {max_accuracy:.2f} (n_estimators={best_n_estimators})')

# 정확도 그래프 출력
plt.plot(n_estimators_list, accuracies)
plt.xlabel('n_estimators')
plt.ylabel('Accuracy')
plt.title('RandomForest Accuracy by n_estimators')
plt.show()

# 의사결정 트리 시각화
rfc = RandomForestClassifier(n_estimators=best_n_estimators, random_state=42)
rfc.fit(X_train, y_train)
model = rfc.estimators_[5]  # 예시로 5번째 트리 선택

dt_dot_data = tree.export_graphviz(model,
                                   feature_names=iris.feature_names,
                                   class_names=iris.target_names,
                                   filled=True, rounded=True,
                                   special_characters=True)
dt_graph = pydotplus.graph_from_dot_data(dt_dot_data)
Image(dt_graph.create_png())

# 임의의 데이터에 대한 예측
myX_test = np.array([[5.6, 2.9, 3.6, 1.3]])
myprediction = rfc.predict(myX_test)
predicted_class = iris.target_names[myprediction][0]
print(f'임의의 데이터는 다음 Iris 종에 속합니다: {predicted_class}')