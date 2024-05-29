# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:13:59 2024

@author: doris
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터를 읽어온다.
df = pd.read_csv('age.csv', encoding='cp949', thousands=',')
df = df.replace(',', '', regex=True)  # 쉼표 제거

# 궁금한 지역 이름
name = '강남구 대치1동'

# 입력받은 지역의 인구 구조 (비율로 변환)

# 입력받은 지역의 인구 구조 (비율로 변환)
home_data = df[df['행정구역'].str.contains(name)].iloc[:, 3:].astype(int)
home_total = home_data.sum(axis=1).values  # 이것은 배열이 됩니다.
home_ratio = home_data.div(home_total[0], axis=0)  # 스칼라 값으로 나눕니다.

# 유사한 인구 구조를 가진 지역 찾기
results = []

for idx, row in df.iterrows():
    if name not in row['행정구역']:
        away_data = row[3:].astype(int)
        away_total = away_data.sum()
        away_ratio = away_data / away_total  # 비율 계산
        # 차이의 제곱의 합을 계산한다.
        diff_sum = np.sum((home_ratio.values.flatten() - away_ratio) ** 2)
        # 결과 리스트에 추가한다.
        results.append((row['행정구역'], diff_sum, away_ratio))

# 가장 차이가 작은 5개 지역을 가져온다.
results.sort(key=lambda x: x[1])
top_five = results[:5]

# 결과 출력 및 시각화
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역 TOP 5')

# 입력받은 지역의 인구 구조 그리기
plt.plot(home_ratio.values.flatten(), label=name)

# 유사한 인구 구조를 가진 5개 지역 그리기
for area_name, _, area_data in top_five:
    plt.plot(area_data, label=area_name)

plt.legend()
plt.show()
