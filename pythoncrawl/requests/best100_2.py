# 다음 쇼핑 베스트 100에서 임의의 카테고리 2개를 정해서
# 정보를 가져온 뒤 상품명 출력하기
import requests
# url_food = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=D01&durationDays=30&count=100&_=1598408319222"
# url_beauty = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=A03&durationDays=30&count=100&_=1598407794216"

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?durationDays=30&count=100"
params = [
    {"vCateId" : "D01", "_" : "1598408319222"}, # 식품
    {"vCateId" : "A03", "_" : "1598407794216"}, # 화장품
]

with requests.Session() as s:
    for param in params:
        res = s.get(url, params=param)
    
        for i, item in enumerate(res.json(), 1):
            if i < 101:
                print(i, item["product_name"])
        print("*" * 30)
        