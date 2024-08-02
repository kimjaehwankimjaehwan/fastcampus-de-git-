### dataprocessing.py : 데이터 처리

# 데이터 처리
# numpy
def p(a):
    print(a, '\n')

import numpy as np
import pandas as pd

# 넘파이 배열 생성
ar1 = np.array([1,2,3,4,5])
ar2 = np.array([[1,2,3] ,[4,5,6]])
print(ar1)
print(ar2)

ar3 = np.arange(1,6)
ar4 = np.arange(1,7).reshape(2,3)
print(ar3)
print(ar4)

# 3개의 랜덤값을 가진 배열을 생성
ar3 = np.random.randn(3)
# 2행 3열 의 랜덤값을 가진 2차원 배열을 생성
ar4 = np.random.randn(2,3)
# 2,3,3, 랜덤값을 가진 3차원 배열을 생성
ar5 = np.random.randn(2,3,3)

p(ar3)
p(ar4)
p(ar5)

ar6 = np.zeros(5) # 1차원 5개의 0
ar7 = np.zeros((2,5,5)) # 3차원(2개 차원, 5행, 5열)의 0
ar8 = np.ones(5) # 1차원 5개의 1
ar9 = np.ones((5,5)) # 2차원 5행 5열의 1
p(ar6)
p(ar7)
p(ar8)
p(ar9)

# 20부터 200전까지 10씩 증가하는 1차원 배열
ar7 = np.arange(20,200,10)
p(ar7)
# 3행 6열로 형태변경
ar8 = ar7.reshape(3,6)
p(ar8)

ar1 = np.arange(1, 11, 1) # 1~10까지 1차원 배열
ar2 = ar1 + 3 # 각 요소에 3을 더함
ar3 = ar1 * 2 # 각 요소에 2를 곱합
p(ar1)
p(ar2)
p(ar3)

ar1 = np.array([[5,7,9],[-7,-6,19],[6,9,11]])
p(ar1)
p(ar1.sum()) # 전체 합계
p(ar1.mean()) # 산술 평균
p(ar1.max()) # 최대값
p(ar1.min()) # 최소값
p(ar1.max(axis=0)) # 각열의 요소 중 가장 큰 값
p(ar1.max(axis=1)) # 각행의 요소 중 가장 큰 값

ar1 = np.array([[5,7,9],[-7,-6,19],[6,9,11]])
p(ar1 >0) # 0보다 크면 True, 아니면 False
p(ar1[ar1 >0])
m_count = (ar1 <0).sum()
p(m_count)

m_sum = ar1[ar1<0].sum()
p(m_sum)

# where : 조건 , where(조건, 조건이 True , 조건이 False
ar2 = np.where(ar1<0 , 0, ar1)
p(ar2)

ar1 = np.array([[5,7,9],[-3,-6,19],[6,4,11]])
p(ar1)
ar1.sort(0) # 열단위로 정렬
p(ar1)
ar1.sort(1) # 행단위로 정렬
p(ar1)


# pandas

import pandas as pd

# series : 인덱스를 가진 1차원 데이터
sr1 = pd.Series([10, 30, 20, 40, 60])
p(sr1)
p(sr1[2])
p(sr1[[1,2]]) # 서브시리즈
p(sr1.index)
p(sr1.values)
p(type(sr1.values))

# 인덱스를 문자로 지정
sr1 = pd.Series([10,30,20,40,60], index = ['a','b','c','d','e'])
p(sr1)
p(sr1['b'])
p(sr1[['a','b']]) # 서브시리즈
p(sr1['b':'d']) # 서브시리즈 (슬라이싱 이용)

# DateFrame
df1 = pd.DataFrame([[10,20,30],[40,50,60]])
p(df1)

dict = {'name':["홍길동",'강감찬'],"age":[20,30]}
df2 = pd.DataFrame(dict)
p(df2)

# 인덱스 설정
df2 = pd.DataFrame(dict, index=['a','b'])

df2.rename(columns={'name':'이름', 'age':'나이'}, inplace=True)
df2.rename(index={'0':'1행', '1':'2행'}, inplace=True)
p(df2)













