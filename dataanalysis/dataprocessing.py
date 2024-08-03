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
# Series : 인덱스가 있는 1차원 데이터
# DataFrame : 2개 이상의 Series의 집합인 2차원 데이터
p(type(df['kor']))

p(df[["eng", "math"]])
p(type(df[["eng", "math"]]))

# # 인덱스에 따라 내림차순 정렬
# df_score_sorted = df["math"].sort_index(ascending=False)
# p(df_score_sorted)
#
# # 인덱스에 따라 오름차순 정렬
# df_score_sorted = df["math"].sort_index()
# p(df_score_sorted)
#
# # 값에 따라 내림차순 정렬
# df_score_sorted = df["math"].sort_values(ascending=False)
# p(df_score_sorted)
#
# # 값에 따라 오름차순 정렬
# df_score_sorted = df["math"].sort_values()
# p(df_score_sorted)


# 변수 제거
p(df.drop(columns = "math"))
p(df)

# df = p(df.drop(columns = "math"))
# p(df)

p(type(df))
p(df.info())
# 함수 조합
p(df.query("nclass==2")[["kor"]])
p(df.query("nclass==2")[["kor"]].head(2))

# 데이터 정렬
p(df)
p(df.sort_values("kor"))
p(df.sort_values("kor", ascending=False))

# 새로운 변수( 파생변수) 추가
totaldf = df.assign(total = df["kor"] + df["eng"] + df["math"])
p(totaldf)

# df['total'] = df["kor"] + df["eng"] + df["math"]
# p(df)

meandf = totaldf.assign(mean = (sum(totaldf['total']))/3)
p(meandf)

# 파생변수 추가시 조건 부여
import numpy as np
resultdf = meandf.assign(result = np.where(meandf['mean']>=60,"pass","fail"))
p(resultdf)

# 그룹핑
# agg : 집계함수(개수, 총점, 평균...)
p(df.agg(mean_math = ("math", "mean"))) # math 평균
p(df.agg(mean_math = ("math", "count"))) # math 개수
p(df.agg(mean_math = ("math", "median"))) # math 중앙값
p(df.agg(mean_math = ("math", "min"))) # math 최소값
p(df.agg(mean_math = ("math", "max"))) # math 최대값
# nclass 가 같은 것들을 그룹핑한 후 math 평균
p(df.groupby("nclass", as_index=False).agg(mean_math=("math", "mean")))
# nclass 가 같은 것들을 그룹핑한 후 여러 통계 확인
p(df.groupby("nclass", as_index=False).agg(
    mean_math=("math", "mean"),
    sum_math=("math", "sum"),
    median_math=("math", "median"),
    count_math=("math", "count")
))

# 데이터 합치기
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "mid": [100, 90, 80]
})
p(df1)
df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "final": [90, 80, 70]
})
p(df2)

#행합치기
# NaN (Not a Number) : 숫자가 아니라는 숫자
p(pd.concat([df1, df2]))

# 열 합치기
p(pd.merge(df1 , df2 , how="left", on="id"))
p(pd.merge(df1 , df2 , how="right", on="id"))
p(pd.merge(df1 , df2 , how="inner", on="id"))
p(pd.merge(df1 , df2 , how="outer", on="id"))
p(pd.merge(df1 , df2 , how="cross")) ## on 파라미터 생략 , 가능한 모든 조합을 산출

















