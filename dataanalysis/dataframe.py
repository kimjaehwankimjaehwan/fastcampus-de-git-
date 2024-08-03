# dataframe.py

def p(str):
    print(str, '\n')

# pandas 라이브러리 임포드
import pandas as pd
import numpy as np

# DataFrame 생성
df = pd.DataFrame({
    'name':['홍길동','강감찬','이순신'],
    'kor': [90,80,70],
    'eng': [100,90,80],
    'math': [60,50,40]
})

p(df)

# name 변수의 값
p(df['name'])
p(type(df['name']))

# kor 변수의 합
p(sum(df['kor']))
p(sum(df['kor'])/3)

# 엑셀파일로 DataFrame 생성 후 출력
# openpyxl 외부라이브러리 필요

