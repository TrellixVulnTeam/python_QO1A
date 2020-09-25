# urllib.parse 안 urlencode() 사용하기
# urlencode() - 파라메터 값 넘길 때 주로 사용
# https://naver.com?search=영화      / search=영화 --> 파라메터

from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org"
values = {"format":"json"}  # dict 구조

print("before param : {}".format(values))
params = urlencode(values)  # dict 구조를 encode 함
print("after param : {}".format(params))

url = api + "?" + params
print("요청 URL = {}".format(url))

response = urlopen(url).read().decode("utf-8")
print(response)
