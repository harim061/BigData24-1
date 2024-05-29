# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:50:38 2024

@author: doris
"""

import csv
import matplotlib.pyplot as plt
import heapq

f = open('age.csv')

data = csv.reader(f)
next(data)
data = list(data)

name='강남구 대치1동'

# 입력받은 지역의 인구 구조를 저장한다.
for row in data:
    if name in row[0]:  # 입력 받은 지역의 이름이 포함된 행 찾기
        home = [int(value.replace(',', '')) for value in row[3:]]
        home_total = int(row[2].replace(',', ''))
        home = [val/home_total for val in home]  # 비율로 변환
        break

# 유사한 인구 구조를 가진 지역을 찾는다.
# (차이의 제곱의 합, 지역 이름, 지역 인구 비율)을 저장할 힙 생성
heap = []

for row in data:
    if name not in row[0]:  # 같은 지역은 비교하지 않는다.
        away = [int(value.replace(',', '')) for value in row[3:]]
        away_total = int(row[2].replace(',', ''))
        away = [val/away_total for val in away]  # 비율로 변환
        # 차이의 제곱의 합을 계산한다.
        diff_sum = sum((h - a) ** 2 for h, a in zip(home, away))  # sum 변수 이름 변경
        # 힙에 저장한다. 차이가 작을수록 먼저 나오도록 저장한다.
        heapq.heappush(heap, (diff_sum, row[0], away))

# 가장 차이가 작은 5개 지역을 가져온다.
top_five = heapq.nsmallest(5, heap)

# 결과 출력 및 시각화
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역 TOP 5')

# 입력받은 지역의 인구 구조 그리기
plt.plot(home, label=name)

# 유사한 인구 구조를 가진 5개 지역 그리기
for diff_sum, area_name, area_data in top_five:
    plt.plot(area_data, label=area_name)

plt.legend()
plt.show()