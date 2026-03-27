import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import numpy as np  
import seaborn as sns
import matplotlib.pyplot as plt

# snow의 3년 데이터 CSV추출하기
# 2020년 9월 16일 상장
snow_df = yf.download("snow", "2021-02-01", "2024-02-02")
snow_df.info()


snow_df.to_csv("snow_2y.csv", index=False)

# 3개년 시가 및 종가 데이터 + 거래량 추이
plt.figure(figsize=(12, 6)) 
sns.scatterplot(data = snow_df, x = 'Date',y = 'Open',  color='blue', label='open')
sns.scatterplot(data = snow_df, x = 'Date',y = 'Adj Close', color='orange', label='Adj Close')
plt.figure(figsize=(12, 6)) 
sns.lineplot(data = snow_df, x = 'Date',y = 'Volume',  color='red', label='Volume')
plt.legend()
plt.show()
