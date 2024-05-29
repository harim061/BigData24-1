# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:34:00 2024

@author: doris
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


 df = pd.read_csv('weather_data.csv')

def fetch_weather():
    # 기상청 도시별 관측 페이지
    url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 데이터 추출을 위한 리스트 초기화
    data = []
    
    # 테이블에서 각 행(도시별 데이터) 추출
    table = soup.find('table', {'class': 'table-col'})
    for row in table.find_all('tr')[2:]:  # 헤더 제외
        th = row.find('th', {'class': 'border-right-gray-1'})
        if th:
            station_link = th.find('a')
            station = station_link.text.strip() if station_link else 'No station name'
    

        cols = row.find_all('td')
        if cols:
            
            temperature = cols[4].text.strip()  # 온도 데이터 위치
            humidity = cols[9].text.strip()  # 습도 데이터 위치
            data.append([station, temperature, humidity])
    
    return data

def main():
    weather_data = fetch_weather()
    weather_df = pd.DataFrame(weather_data, columns=['sido-gu', '온도', '습도'])
    # 결과 DataFrame을 CSV 파일로 저장
    weather_df.to_csv('weather_data.csv', encoding='utf-8-sig', index=False)
    print(weather_df)  # 결과 확인을 위한 출력
    df = pd.read_csv('weather_data.csv') 

if __name__ == '__main__':
    main()
