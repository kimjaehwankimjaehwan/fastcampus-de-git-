# dataprocessing.py

def p(str):
    print(str, "\n")

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "name": ["kim", "lee", "park", "choi", "hong"],
        "nclass": [1, 1, 2, 2, 2],
        "kor": [10, 20, 30, 40, 50],
        "eng": [30, 40, 50, 60, 70],
        "math": [50, 60, 70, 80, 90]
    }
)
p(df)

# 조건에 맞는 행 검색  ## 왠지 SQL 문이 생각남
p(df.query("kor==10")) ## "" 사이에 조건을 넣어야 함
p(df.query("kor!=10"))
p(df.query("eng>50"))
p(df.query("nclass==1 & eng >=40"))
p(df.query("nclass==1 | eng >=40"))
p(df.query("kor in [10, 30, 50]"))

# 파이썬 변수를 조건에 사용가능
korList = [10, 30, 50]
p(df.query("kor in @korList"))

# 특정 변수만 추출
p(df["kor"])
# Series : 인덱스가 있는 1차우너 데이터
# DataFrame : 2개 이상의 Series의 집합인 2차우너 데이터
p(type(df['kor']))

















