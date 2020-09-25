import requests

s = requests.Session()

# payload = {"id":"seng322", "password":"wooni94"}
param = {"id":"seng322", "password":"wooni94"}

# res = s.post("http://httpbin.org/post", data=payload)
res = s.get("http://httpbin.org/get", params=param)

# raise_for_status() : 상태 체크를 한 후 이상이 발생하면 다음 문장을 처리 안함
res.raise_for_status()
print(res.text)

s.close()
