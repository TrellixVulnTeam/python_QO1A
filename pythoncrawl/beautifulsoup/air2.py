import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"

param = {
    "serviceKey" : unquote("xi2PeqbCLzhL8NDeHy1uHD%2B%2BBQxcnfkvxjmp2YVtHkJFY4QxzlWFowPTqTLHZuBTD%2Fk%2BeZ7nmnH3MJBJCZJmYw%3D%3D"),
    "stationName" : "중랑구",
    "dataTerm" : "DAILY"
}

res = requests.get(url, params=param)
# print(res.text)
soup = BeautifulSoup(res.content, "html.parser")

# select, select_one, find, find_all 중 css선택자를 사용하는 select계열 사용불가능
data = soup.find_all("item")
for item in data:
    print(item.get_text())
