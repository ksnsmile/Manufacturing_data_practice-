# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:29:34 2024

@author: sn714
"""

import pandas as pd

df1=pd.read_csv('C:/Users/sn714/OneDrive/바탕 화면/error_message.csv')
df1.head(3)

df1.info()

# 기술 통계량 확인(그 데이터가 연속형인지 범주형인지 등)

df1.describe() # 숫자 데이터 확인 방법

#범주형 데이터 확인 방법

df1['메세지'].unique()

df1['메세지'].value_counts()

df1.describe(include='object') # 법주형 데이터 describe