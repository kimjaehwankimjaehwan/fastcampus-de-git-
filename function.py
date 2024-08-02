# function (함수)
# 입력값들을 받아서 어떤 처리를 하고 출력값을
# 반환하는 코드 블럭

def add(a, b):
    return a + b


print(add(3, 5))
print(add('hello', 'python'))


# print(add())
# print(add(3, 5, 7))


def multi(a, b=3):  # b파라미터 값이 전달이 안되면 3으로
    return a * b


print(multi(5, 5))
print(multi(5))

# 람다 함수
# 일회만 사용할 목적으로 이름 없이 lambda 키워드를 사용하는 함수
# def 생략, lambda 파라미터리스트 : 코드블럭
lambda_add = lambda a, b: a + b
print(lambda_add(3, 3))


# lambda 함수를 생성해서 변수에 대입

# lambda 함수는 값(value)이므로 변수에 저장하는 것이 가능
# 람다 함수는 함수의 파라미터로 전달하는 것이 가능
def calc(a, b, func):  # 파라미터로 전달된 함수를 콜백함수라고 부른다.
    return func(a, b)


func1 = lambda a, b: a + b
print(calc(3, 5, func1))

func2 = lambda a, b: a * b
print(calc(3, 5, func2))

# 



