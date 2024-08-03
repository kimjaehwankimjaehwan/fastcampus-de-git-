import pandas as pd
import numpy as np
import openpyexcel as opx

def p(str):
    print(str, '\n')

exam = pd.read_csv("../assets/exam3.csv")
p(exam)

# 상위 5행
p(exam.head())

# 상위 10행
p(exam.head(10))

# 하위 5행
p(exam.tail())

# 하위 10행
p(exam.tail(10))

# 행의 수, 열의 수
p(exam.shape)

# 변수 속성 출력
p(exam.info())

df = pd.read_csv("../assets/economics.csv")
p(df)

# 상위 10 행
p(df.head(10))
# 하위 10 행
p(df.tail(10))
# 행의수, 열의수
p(df.shape)
# 변수 속성 출력
p(df.info())
# 기술통계
p(df.describe())
p(df.describe(include = "object"))

df['date'] = pd.to_datetime(df['date'])

# 변수 속성 출력
p(df.info())
# 기술통계
p(df.describe())
# p(df.describe(include = "object"))

p(df)

p(exam.describe())
p(exam.describe(include = "all"))

# 실습용 DataFrame 생성
df_org = pd.DataFrame({
    'var1': [1, 2, 1],
    'var2': [2, 3, 2]
})
p(df_org)

# 변수명 변경
df_new = df_org.rename(columns={'var1': 'data1'})
p(df_new)

# 새로운 변수(파생변수) 생성
df_new["data2"] = df_new["data1"] + df_new["var2"]
p(df_new)

# 그래프 출력을 위해 matplotlib 외부라이브러리 필요

df_score = pd.DataFrame({
    'name': ['홍길동', '강감찬', '이순신'],
    'kor': [90, 80, 70],
    'eng': [100, 90, 80],
    'math': [60, 50, 40]
})

# import matplotlib.pyplot as plt
# df_score.boxplot(column=['kor','eng','math'])
# plt.show()


# 필요한 패키지 불러오기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

# 운영체제에 따른 폰트 설정
if platform.system() == 'Windows':
    font_path = 'C:/Windows/Fonts/malgun.ttf'  # 윈도우에서는 '맑은 고딕' 폰트 경로
elif platform.system() == 'Darwin':  # MacOS
    font_path = '/System/Library/Fonts/AppleGothic.ttf'
else:
    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # 리눅스에서는 나눔 폰트 경로

# 폰트를 matplotlib에 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 한글 폰트가 제대로 설정되었는지 확인
# plt.rcParams['axes.unicode_minus'] = False
# plt.title('테스트')
# plt.plot([1, 2, 3], [1, 4, 9])
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# plt.figure(figsize = (12,8))
# sns.histplot(exam, bins=10)
# # X축 레이블 설정
# plt.xticks(rotation=45)
# plt.show()



# numpy를 활용한 DataFrame 조건 부여
import numpy as np
df_score["test"] = np.where(df_score["math"]>60, "pass", 'fail')
p(df_score)

# 조건에 따른 pass, fail 개수
counts = df_score["test"].value_counts()
p(counts)

# 조건 중첩 (np.where - SQL 구문과 동일)
df_score["grade"] = np.where(df_score['math']>=60, "A",
                             np.where(df_score['math'] >= 50, "B", "C")
                    )
p(df_score)

# 인덱스에 따른 오름차순 정렬
df_score_sorted = df_score["math"].sort_index(ascending=False)
p(df_score_sorted)

# 인덱스에 따른 내름차순 정렬
df_score_sorted = df_score["math"].sort_index()
p(df_score_sorted)

# 값에 따른 오름차순 정렬
df_score_sorted = df_score["math"].sort_values(ascending=False)
p(df_score_sorted)

# 값에 따른 내름차순 정렬
df_score_sorted = df_score["math"].sort_values()
p(df_score_sorted)


