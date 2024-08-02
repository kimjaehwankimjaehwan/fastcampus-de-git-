### remotejsondata.py

## 원격 서버의 JSON 데이터 처리

# requests, json
import requests
import json

# get 요청으로 JSON 데이터 불러오기
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()
# print(data)

# post 요청으로 JSON 데이터 등록
# 딕셔너리로 데이터 생성
sendData = {
    "userId":101,
    "id":101,
    "title": "sample title",
    "body" : "sample body sample body sample body"
}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    sendData
)
# print(response.text)

# urllib
# 200:OK, 403 : Forbbiden, 404: Not Found , 500:Server Error
from urllib.request import urlopen

# url에 연결
response = urlopen('https://jsonplaceholder.typicode.com/posts')
# 응답이 성공했다면
if response.getcode() == 200: # OK (서버에서 정상적으로 응답했다는 응답코드)
    # 응답 데이터를 utf-8 형태로 수신
    data = json.loads(response.read().decode('utf-8'))
    for post in data:
        print(post['title'])
else :
    print('에러!')

# 동기통신과 비동기통신
# 동기통신(Synchronous Communication)
#   요청 후 응답을 대기하는 통신 방식
#   장점 : 응답의 순서를 알 수 있다. (= 다음 요청때 이전 응답의 결과를 사용할 수 있다.)
#   단점 : 속도가 비동기통신에 비해 느림, blocking위험(응답이 안오는 경우에 다음 요청 불가)

# 비동기통신(Asyncronous Communication)
#   요청 후 응답을 대기하지 않고 바로 다음 요청을 하는 통신 방식
#   장점 : 속도가 동기통신에 비해 빠름
#   단점 : 응답의 순서를 알 수 없다. (=다음 요청때 이전 응답의 결과를 사용할 수 없다.)

# aiohttp, asyncio(동기통신방식)
import aiohttp
import asyncio

# 데이터 가져오는 비동기 함수 
async def fetch_json(url):
    # 연결(Session)을 생성
    async with aiohttp.ClientSession() as session:
        # 세션을 통해서 URL의 데이터를 가져옴
        async with session.get(url) as response:
            data = await response.json()
            return data

# 비동기함수를 호출하는 비동기 함수
async def main():
    # 호출할 URL 저장
    url = 'https://jsonplaceholder.typicode.com/posts'
    # 비동기로 URL의 데이터를 호출
    # await : 비동기 처리 중에 동기처리 해야되는 코드 앞에 사용하는 키워드
    #         fetch_json(url)의 결과가 나오면 data에 저장함
    #         blocking method (처리완료를 보장하는 메소드)
    data = await fetch_json(url)
    # 들여쓰기 4칸 하면서 data를 출력
    print(json.dumps(data, indent=4))

asyncio.run(main())

def a(b,c):
    result = b+c
    return result

# 실습 : aiohttp 모듈을 이용해서 'https://jsonplaceholder.typicode.com/users'
# 데이터를 로딩한 후에 사용자의 이름과 전화번호를 출력하는 프로그램 작성

# aiohttp, asyncio(동기통신방식)
import aiohttp
import asyncio

# 데이터 가져오는 비동기 함수
async def fetch_json2(url):
    # 연결(Session)을 생성
    async with aiohttp.ClientSession() as session:
        # 세션을 통해서 URL의 데이터를 가져옴
        async with session.get(url) as response:
            data = await response.json()
            return data

async def main2():
    # 호출할 URL 저장
    url = 'https://jsonplaceholder.typicode.com/users'
    # 비동기로 URL의 데이터를 호출
    # await : 비동기 처리 중에 동기처리 해야되는 코드 앞에 사용하는 키워드
    #         fetch_json(url)의 결과가 나오면 data에 저장함
    #         blocking method (처리완료를 보장하는 메소드)
    response = await fetch_json(url)
    for dict in response:
        print(dict['name'], dict['phone'])

asyncio.run(main2())







