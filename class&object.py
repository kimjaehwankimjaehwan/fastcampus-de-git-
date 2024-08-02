# class : template of object, 객체를 생성하는 틀(설계도)
# object : 클래스를 통해서 생성되는 변수와 메서드의 집합
# self : 클래스를 통해서 생성되는 객체 자신 ( 다른 언어들은 this)
# 생성자는 __init__이란 이름을 사용하고 만들어진느 객체의 변수를 초기화


# 클래스 생성
# 클래스명은 대문자로 시작
class Human:
    humanCount = 0 # 클래스 변수 (객체들이 공통으로 공유하는 변수)
    def __init__(self, name, age): # 생성자
        self.name = name # 객체의 name 변수 = 생성자 파라미터 name 변수
        self.age = age
        self.id = Human.humanCount
        Human.humanCount += 1

    def setAge(self, age): # 메소드 (setter : 객체변수의 값을 변경)
        self.age = age

    def getAge(self):  # 메소드 (getter : 객체변수의 값을 가져옴)
        return self.age


hong = Human( "홍길동", 20)
print(hong.name)
print(hong.getAge())
hong.setAge(35)
print(hong.getAge())

yoon = Human("윤석렬" , 58)
print(yoon.name)
print(yoon.getAge())
yoon.setAge(60)
print(yoon.getAge())

# 또다른 객체 생성
kang = Human("강감찬", 30)
print(kang.humanCount)
print(kang.name)
print(kang.age)

# 객체로 접근하면 클래스 변수가 아니라 객체 변수
kang.humanCount = 1
print(hong.humanCount)

# 클래스로 접근
Human.humanCount = 1
print(hong.humanCount)
print(kang.humanCount)

# 상속 & 오버라이딩
class Vehicle:
    def __init__(self, name, tireCount):
        self.name = name
        self.tireCount = tireCount
    def getName(self):
        return f"이 탈것의 이름은 {self.name}입니다."

class Car(Vehicle):
    def getName(self):
        return f'이 차의 이름은 {self.name}입니다.'

car = Car("Bentz", 4)
print(car.name, car.tireCount)

car = Vehicle("BMW" ,4 )
print(car.getName())

car = Car("BMW" ,4 )
print(car.getName())


# 오버라이딩

class Bird():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def cry(self):
        print(f"새는 {self.sound} 소리를 냅니다.")

class Eagle(Bird):
    def cry(self):
        print(f"{self.name}는 {self.sound} 소리를 냅니다.")

class Hen(Bird):
    def cry(self):
        print(f"{self.name}는 {self.sound} 소리를 냅니다.")

class Duck(Bird):
    def cry(self):
        print(f"{self.name}는 {self.sound} 소리를 냅니다.")

eagle = Eagle("독수리", "꽤꽤")
hen = Hen("닭", "꼬끼오")
duck = Duck("오리", "꽥꽥")
eagle.cry()
hen.cry()
duck.cry()

birdList = [
    Hen( "닭1", "꼬끼오"),
    Hen("닭2", "꼬끼오"),
    Eagle("독수리1", "꽤꽤"),
    Eagle("독수리2", "꽤꽤"),
    Duck("오리1", "꽥꽥"),
    Duck("오리2", "꽥꽥")
]

for bird in birdList:
    bird.cry()

# 객체지향의 3대 개념

# 1. 상속(Inheritance)
# 기존에 잘 만들어진 것들을 재사용(reusing)

# 2. 다형성(Polymophism)
# 동일한 형태인데 다른 성질을 갖도록
# 예) 오버라이딩

# 3. 추상화(Abstraction)
# 본연의 성질을 잃지 않는 선에서 최대한 단순화
# 예) 클래스 

