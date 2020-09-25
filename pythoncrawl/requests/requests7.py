import requests

# timeout 속성 : 특정 사이트에 시간을 지정하고 데이터가 시간 안에 응답하지 않는 경우 Error 발생하도록 함
with requests.Session() as s:
    res = s.get("https://api.github.com/events", timeout=0.001)
    print(res.text)
