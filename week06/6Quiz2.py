# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:22:45 2024

@author: doris
"""

import matplotlib.pyplot as plt
import json

# JSON 파일 읽기
with open('중국_방한외래관광객_2018_202412.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 날짜와 입국자 수 추출
dates = [item['yyyymm'] for item in data]
visitors = [item['visit_cnt'] for item in data]

# 막대그래프 그리기
plt.figure(figsize=(10, 8))  # 그래프 크기 설정
plt.bar(dates, visitors, color='skyblue')  # 막대그래프 생성
plt.xlabel('Date (YYYYMM)')  # x축 라벨
plt.ylabel('Number of Visitors')  # y축 라벨
plt.title('Monthly Number of Visitors from China to Korea')  # 그래프 제목
plt.xticks(rotation=90)  # x축 레이블 회전
plt.tight_layout()  # 레이아웃 조정
plt.show()  # 그래프 표시
