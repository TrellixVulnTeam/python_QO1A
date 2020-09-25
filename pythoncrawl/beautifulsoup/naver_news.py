import requests
from bs4 import BeautifulSoup
import  pprint # json을 예쁘게 출력하기

naver_open_api = "https://openapi.naver.com/v1/search/news.json"
param = {"query" : "android"}
headers = {
    "X-Naver-Client-Id" : "KQVDVE9WTmyEUGaxiNGU",
    "X-Naver-Client-Secret" : "bOON5T41cC"
}

res = requests.get(naver_open_api, params=param, headers=headers)
# print(res.json())

data = res.json()  # json.loads(data)

# print(data["items"])
# print(data["items"][0])
# print()
# pprint.pprint(data["items"][:2])

for idx, item in enumerate(data['items'],1):
    print(idx, item["title"], item["link"])
