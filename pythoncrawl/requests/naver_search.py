import requests

# urlopen1.py 변형
# requests 라이브러리를 이용하여 변경해보기

search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&"

param = {"query" : "영화"}

# param = urlencode(param)
# search_url += param

# try:
#     contents = urlopen(search_url).read().decode("utf-8")
#     print(contents[150000:200000])
# except HTTPError as e:
#     print("에러 발생", e.code)

try:
    contents = requests.get(search_url, params=param)
    print(contents.text[150000:200000])
except Exception as e:
    print("에러 발생", e)
