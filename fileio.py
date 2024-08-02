# console io
# console : keyboard + monitor
# input : 사용자의 키보드 입력을 대기(blocking)하는 함수
# str = input('문자를 입력해 주세요!')
# print(f"입력하신 문자는 {str} 입니다.")
# print(str) ## 문자가  str 변수에 저장됨

# num1 = int(input('첫번째 수를 입력해주세요! : '))
# num2 = int(input('두번째 수를 입력해주세요! : '))
#
# print(num1 + num2)
# print((int(num1) + int(num2)))
#
# def add(a, b, func):
#     func(a , b)
#
# func1 = lambda a, b : a + b
#
# print(add(num1, num2, func1))


# file io(input/output)

# f= open("datafile.txt", "r", encoding = 'utf-8')
# print(f.readline()) # 한줄을 읽어서 문자열로
# f.close()

# 파일읽기
# f = open("datafile.txt", "r", encoding = 'UTF-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.read()) # 전체를 다 읽어서 문자열로
# print(f.readlines()) # 전체줄을 읽어서 리스트로
# f.close()

# 파일 쓰기
# 기존에 파일 내용이 있으면 다 덮어버림
# f = open("datafile.txt", "w", encoding = "utf-8")
# f.write("")
# f.writelines(["Hello", "Python"])
# f.close
#
# f = open("datafile.txt", "r", encoding = "utf-8")
# print(f.read())
# f.close


# JSON 읽고 쓰기
# JSON (JavaScript Object Notation)
# {"키1" : "값1", "키2": "값2"}

dict = '{"name": "홍길동", "age" : 20 , "address" : "서울"}'

f = open("jsonObj.json", 'w', encoding = 'utf=8')
f.write(dict)
f.close()

f = open("jsonObj.json", 'r', encoding = 'utf=8')
print(f.read())
f.close()

class Stock():

    market_name = 'KOSPI' # 클래스 변수

    def __init__(self, name='' , price=0, quantity=0 ):
        self.name = name
        self.price = price
        self.quantity = quantity

    def type(self):
        return "가치주인지 성장주인지 파악합니다."

    def __str__(self):
        return f"종목 : {self.name}, 가격 : {self.price}), 수량 : {self.quantity}"

s = Stock("삼성전자", 80000, 40)
print(s)

class investment_1(Stock):
    def __init__(self, name , price, quantity, investment):
        super().__init__(name, price, quantity)
        self.investment = investment

    def type(self):
        return "가치주 입니다."

    def __str__(self):
        return f"종목 : {self.name}, 가격 : {self.price}), 수량 : {self.quantity}, 투자금 : {self.investment}"

class investment_2(Stock):
    def __init__(self, name , price, quantity, investment):
        super().__init__(name, price, quantity)
        self.investment = investment

    def type(self):
        return "성장주 입니다."

    def __str__(self):
        return f"종목 : {self.name}, 가격 : {self.price}), 수량 : {self.quantity}, 투자금 : {self.investment}"


l = Stock("LG전자", 12000 , 100)
print(l)

iv = investment_1
s = iv("삼성전자", 80000, 40, 3200000)
print(s)
print(s.type())

print(s.market_name)



















