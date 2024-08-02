# logic
# 프로그래밍의 로직은 분기, 반복 두가지 뿐이다.
# 모든 알고리즘들은 분기와 반복의 조합

def p(value):
    print(value, '\n')


# 분기
a = 10
if a > 5:  # 조건이 True 일때
    print("a는 5보다 큽니다")
else:  # 조건이 False 일때
    print("a는 5보다 크지않습니다")

a = 3
if a > 10:
    p("a는 10보다 큽니다.")
elif a > 5:
    p("a는 5보다 큽니다.")
else:
    p("a는 5보다 크지 않습니다.")

for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')
print()
for str in "Hello":
    print(str, end=' ')
print()
for i in range(1, 10):
    print(i, end=' ')
print()

for i in range(10, 21):
    print(i, end=' ')
print()

for i in range(1, 101, 2):  # 1~100까지 홀수만
    print(i, end=' ')
print()

for i in range(0, 101, 7):
    print(i, end=' ')
print()

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i}*{j} = {i * j}', end=' ')
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()

for i in range(1, 6):
    for j in range(1, 7 - i):
        print('*', end='')
    print()

dic = {'a': 1, 'b': 2, 'c': 3}
for i in dic.keys():
    p(i)
for i in dic.values():
    p(i)
for i in dic.items():
    p(i)

nums = list(range(1, 11))
for i in nums:
    if i % 2 == 0:
        continue  # 아래 코드 수행하지 않고 다음번 반복을 수행
    if i == 9:
        break  # 가장 가까운 반복문은 빠져나감
    else:
        p(i)

# 반복 : while
# 조건이 True 동안 계속 반복
# 무한 루프에 빠지지 않도록 (조건이 언젠가는 False가 되도록)

a = 0
while a < 10:
    p(a)
    a = a + 1

a = 0
while a < 10:
    if a == 5:
        break
    p(a)
    a += 1
