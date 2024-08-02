# 예외 (Exception)
# 프로그램 실행 중 발생가능한 에러 중에서 개발자가 처리할 수 있는 에러
# try : 예외 발생 가능한 코드 블럭
# except : 예외 처리 코드 블럭
# finally : 예외 발생 여부와 상관없이 수행할 코드 블럭
# 파일 사용 닫기 등 예외와 상관없이 수행해야 되는 코드들을 finally에 넣어준다.

# result = 10 / 0
#
# try :
#     result = 10 / 0
# except ZeroDivisionError:
#     print("0으로 나누기 예외 발생!")
# finally:
#     print("이 코드는 예외발생 여부와 상관없이 수행됨!")

from Under19Exception import Under19Exception
# 사용자 정의 예외

# class Under19Exception(Exception) :
#     def __str__(self):
#         return "19세 이하 관람불가"
# age = 18
#
# if age < 19 :
#     try :
#         raise Under19Exception
#         result = 10 / 0
#
#     except ZeroDivisionError:
#         print("0으로 나누는 예외가 발생했으나 무시함")
#     except Under19Exception:
#         print(Under19Exception())
#         print("19세 이하 관람불가 예외 처리!")
#     finally:
#         print("예외 발생과 상관없이 수행되는 코드")

age = 18

if age < 19:
    try:
        try:
            raise Under19Exception
        except Under19Exception:
            print(Under19Exception())
            print("19세 이하 관람불가 예외 처리!")

        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("0으로 나누는 예외가 발생했으나 무시함")
    finally:
        print("예외 발생과 상관없이 수행되는 코드")






