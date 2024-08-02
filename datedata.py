### datedata.py


## 날짜데이터 처리

def p(str):
    print(str, "\n")

# datetime
import datetime
today = datetime.date.today()
p(today)
p(today.weekday())
p(today + datetime.timedelta(days=100)) # 100일 후
p(today + datetime.timedelta(days=-100)) # 100일 전
p(today + datetime.timedelta(weeks=10)) # 10주 후
p(today + datetime.timedelta(hours=45)) # 45시간 후

day1 = datetime.date(2019, 1 , 1)
day2 = datetime.date(2024, 7, 27)
p(day2 - day1) # 날짜 간격

## calendar
import calendar
p(calendar.weekday(2024, 7, 27)) # 요일
p(calendar.isleap(2024)) # 윤년 여부







