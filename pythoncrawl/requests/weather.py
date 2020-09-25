import requests

weather_url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

# urllib의 urlopen (urlopen1.py 변형)
# data = req.urlopen(weather_url).read()

# requests 라이브러리를 이용하여 변경해보기

# 바로 get 요청하는 방법
# res = requests.get(weather_url)
# print(res.text)

# session을 이용하는 방법
with requests.Session()  as s:
    res = s.get(weather_url)
    print(res.text)
