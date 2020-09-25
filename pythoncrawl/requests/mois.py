import requests

# requests 라이브러리를 이용하여 변경해보기(urlencode4.py 변형)
# 행정안전부 rss 기본 주소
api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
params = []
# dict구조로 만들어서 리스트에 추가
for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))
print(params)

# for c in params:
#     param = urlencode(c)
#     url = api + "?" + param
#     print("url : {}".format(url))
#     # 요청
#     contents = urlopen(url).read().decode("utf-8")
#     print("*" * 50)
#     print(contents)
#     print()

with requests.Session() as s:
    for param in params:
        # 요청
        contents = s.get(api, params=param)
        print("*" * 50)
        print(contents.text)
        print()
