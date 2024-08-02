'''
출력 함수
'''


def p(k):
    print(k, '\n')


# 숫자형
p(1)  # 정수
p(0.1)  # 실수
p(3E5)  # 3곱하기 10의 5승
p(0o10)  # 0o 8진수기호 의미 : 8진수 10
p(0xFF)  # 0x 16진수 :
p(1 + 2)
p(3 ** 3)
p(7 % 4)
p(7 // 4)

# 문자형
p("hello")
p('hello')
p('''
hello
hello
hello
''')

p("Hello 'Tom'")  # 문자열 내에 문자열 사용
p('Hello "Tom"')  # 문자열 내에 문자열 사용
p('Hello "Tom"')  # 문자열 내에 문자열 사용
p("Hello\nTom")  # \n 줄바꿈문자
p("Hello" + "Tom")  # 문자열 접합(concatenation)
p("Hello" * 3)  # 문자열 반복( iteration)
p(len("Hello"))  # 문자열 길이

str = "Hello There"
p(str[0])
p(str[:3])  # 인덱스가 0~2까지의 문자들
p(str[3:])  # 인덱스 3부터 끝까지 문자들
a = list(i for i in str)
p(str[3:5])
p(str[::2]) # 첫문자부터 끝문자까지 step이 2개씩 넘어감

str = "jane"
num =20
import random as rd
rd.shuffle(a)
p("%s은 %d살 입니다." %(str , num))
p('{} 은 {}살입니다.'.format(str,num))
p(f'{str}은 {num}살 입니다.')
p(a)
p("%10s" %"Hello") # 10자리로 표시
p("%10.4f" %3.141592) # 전체 표시자리수는 10자리, 소수점 이하 4자리

str = "hello there"
p(str.count("e")) # e의 개수
p(str.find('e')) # e가 처음나오는 곳의 인덱스
p(str.find('k')) # 해당 문자열이 없으면 -1
p(str.index('e')) # e가 처음나오는 곳의 인덱스
p(str.upper()) # 대문자로 변환
p(str.upper().lower()) # 대문자로 변환 후 소문자로 변환
p(str.replace("e","k")) # 문자열 대체
p(str.split()) # 문자열을 리스트로 변환(기준이 공백문자)
p(str.split("e")) # 문자열을 리스트로 변환(기준이 e문자)
p("010-0000-0000".split("-"))


## List
# 여러 데이터를 하나의 변수에 저장
# 크기가 가변적이고, 어떤 타입의 값도 저장이 가능
# index를 통해서 각각의 데이터에 접근
# index는 0부터 시작, index의 범위는 0~length-1 까지
even = [2,4,6,8]
odd = [1,3,5,7]
print(even, odd)
p(even[0]) # 2
p(even[0:])
p(even[:2])
p(even[::2])
p(even[-1])

p(even + odd)
p(even *3)

p(even.index(6))
p(len(even))

del even[0]
p(even)

even.append(10)
p(even)

even.sort()
p(even)
even.sort(reverse=True)
p(even)
even.reverse()
p(even)

even.insert(0,2)
p(even)
even.remove(2)
p(even)

even.pop() # 맨뒤의 요소 제거
p(even)

even.extend([10, 12]) # 배열의 요소들을 기존배열에 추가
p(even)
even.append([13,14]) # 배열을 그대로 기존배열에 추가
p(even)

even.remove(6)
p(even)

# Tuple (튜플)
# 기본적으로 리스트와 같으나 값을 변경할 수 없음
# 기호를 ()를 사용
day = ('월','화','수','목','금','토','일')
p(day)

# Dictionary(딕셔너리)
# "키:값" 의 형대로 데이터를 저장
# "키값" = 아이템(item)
# 데이터의 기본단위는 아이템
# 키는 중복될 수 없고 , 값은 중복될 수 있음
# 키는 값을 찾기 위한 자료 구조
# 아이템들의 순서가없음인덱스를사용하지않음
dic = {
    "name" : "홍길동",
    "age" : 20,
    "address" : "서울"
}

p(dic)
p(dic["name"])
p(dic.get("name"))

dic["name"] = "이순신"
p(dic)

dic["gender"] = "남"
p(dic)

del dic["gender"]
p(dic)

p(dic.keys()) # 키들을 추출해서 dict_keys를 반환
p(dic.values()) # 값들을 추출해서 dict_values 를 반환

p(list(dic.keys())) # dict_kays를 리스트로 변환
p(list(dic.values())) # dict_values 를 리스트로 변환
p(dic.items()) # 아이템들을 추출해서 dict_items를 반환
p(list(dic.items())) # dict_items를 list로 변환

p("gender" in dic) # 딕셔너리에 gender 라는 키가 있는지 확인

# Set
# 집합, 중복값을 하나만 저장하는 자료구조
# {}로 표시
# 요소들의 순서는 없음 = 인덱스 없음
s= {1,2,3,4,5,1,2,3}
p(s)

s= set(['a', 'b','c'])
p(s)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
p(s1 & s2) # 교집합
p(s1 | s2) # 합집합
p(s1 - s2) # 차집합
p(s2 - s1) # 차입합

# Boolean
# True 또는 False의 값을 저장
# 문자열에 문자가 1개 이상 있으면 True
# 리스트, 튜플에 요소가 1개 이상 있으면 True
# 딕셔너리에 아이템이 1개 이상있으면  True
# 0은 False, 0 이 아니면 True
# None 은 False


p(1==1)
p(2<1)
p(bool('hello'))
p(bool(''))
p(bool([]))
p(bool([1,2,3]))



