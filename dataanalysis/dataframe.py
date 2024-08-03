# dataframe.py

def p(str):
    print(str, '\n')

# pandas 라이브러리 임포트
import pandas as pd
import numpy as np
import openpyexcel as opx

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

df_xl_exam = pd.read_excel("../assets/exam.xlsx")
p(df_xl_exam)

# column = 열 = 속성 = attribute = 변수 = variable 개수
p(len(df_xl_exam))

# CSV 파일로 DataFrame 생성 후 출력
df_csv_exam = pd.read_csv("../assets/exam.csv")
p(df_csv_exam)

# DataFrame을 CSV 파일로
# index=False : CSV 파일로 생성할 때 인덱스는 빼고 생성
df.to_csv("../assets/exam2.csv", index=False)

# JSON파일로 DataFrame 생성 후 출력
df_json_exam = pd.read_json("../assets/exam.json")
p(df_json_exam)

# DataFrame을 JSON 파일로
# indent = 4 :들여쓰기를 스페이스 4개로
df.to_json("../assets/exam2.json", indent=4)
p(df_json_exam)

# XML 파일로 DataFrame 생성후 출력
# lxml 외부라이브러리 필요
df_xml_exam = pd.read_xml("../assets/exam.xml")
p(df_xml_exam)

# DataFrame을 XML로
df.to_xml("../assets/exam2.xml", index = False)







