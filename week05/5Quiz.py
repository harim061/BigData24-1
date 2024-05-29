# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:15:23 2024

@author: doris
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from matplotlib import rc

def read_data(file):
    f = open(file, encoding='UTF-8')
    data = csv.reader(f)
    header = next(data)
    num_time_zones = (len(header)-4) // 2
    
        
    # 각 시간대별 승차 및 하차 인원을 저장할 변수 초기화
    total_boarding_counts = [0] * num_time_zones
    total_alighting_counts = [0] * num_time_zones
    
    for row in data:
        for i in range(4, len(row), 2):
            try:
                # 현재 시간대의 승차 및 하차 인원 추출
                boarding_count = int(row[i])
                alighting_count = int(row[i + 1])
            except ValueError:
                # 정수로 변환할 수 없는 경우 건너뜀
                continue
            # 승차 및 하차 인원 집계
            total_boarding_counts[i // 2 - 2] += boarding_count
            total_alighting_counts[i // 2 - 2] += alighting_count
    return total_boarding_counts, total_alighting_counts

boarding_2018, alighting_2018 = read_data('2018년 03월  교통카드 통계자료.csv')
boarding_2020, alighting_2020 = read_data('2020년 03월  교통카드 통계자료.csv')
boarding_2023, alighting_2023 = read_data('2023년 03월  교통카드 통계자료.csv')

rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False
            

plt.figure(figsize=(10,6), dpi=100)
plt.plot(boarding_2018, label='201803 승차')
plt.plot(alighting_2018, label='201803 하차', linestyle='--')
plt.plot(boarding_2020, label='202003 승차')
plt.plot(alighting_2020, label='202003 하차', linestyle='--')
plt.plot(boarding_2023, label='202303 승차')
plt.plot(alighting_2023, label='202303 하차', linestyle='--')
plt.title('지하철 시간대별 승하차 인원 추이(단위 1000만명)')

plt.legend()

plt.xticks(np.arange(24), range(4, 28))
plt.show()
