# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:42:04 2024

@author: doris
"""

import pandas as pd

# 파일 불러오기
df_2014 = pd.read_csv('201402.csv', encoding='cp949')
df_2024 = pd.read_csv('202402.csv', encoding='cp949')

# 지역 이름에서 괄호 제거
df_2014['행정구역'] = df_2014['행정구역'].str.split(' \(').str[0]
df_2024['행정구역'] = df_2024['행정구역'].str.split(' \(').str[0]

df_2014['2014년02월_총인구수'] = df_2014['2014년02월_총인구수'].str.replace(',', '').astype(int)
df_2024['2024년02월_총인구수'] = df_2024['2024년02월_총인구수'].str.replace(',', '').astype(int)

df_merge = pd.merge(df_2014[['행정구역', '2014년02월_총인구수']], df_2024[['행정구역', '2024년02월_총인구수']], on='행정구역')

df_merge['인구 변동'] = df_merge['2014년02월_총인구수'] - df_merge['2024년02월_총인구수']

# 결과 출력
print(df_merge[['행정구역', '인구 변동']])

# 바 차트로 시각화

import matplotlib.pyplot as plt

plt.bar(df_merge['행정구역'], df_merge['인구 변동'])
plt.title('2014년 대비 2024년 지역별 인구 변동')
plt.xlabel('행정구역')
plt.ylabel('인구 변동')
plt.xticks(rotation=90)
plt.tight_layout()

# 차트 저장
plt.savefig('population_change_bar_chart.png', dpi=300)
plt.show()