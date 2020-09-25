import requests

s = requests.Session()

res = s.get("http://httpbin.org/cookies", cookies={"name":"seng"})
print(res.text)
s.close()
