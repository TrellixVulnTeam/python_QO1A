# 다음 쇼핑 베스트 100에서 임의의 카테고리 2개를 정해서
# 정보를 가져온 뒤 상품명 출력하기
import requests
# url_food = "https://shoppinghow.kakao.com/siso/p/api/bestRank/prodbest?cateId=102104108&durationDays=30&count=100&_=1598407761062"
# url_beauty = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=A03&durationDays=30&count=100&_=1598407794216"
urls = [
    "https://shoppinghow.kakao.com/siso/p/api/bestRank/prodbest?cateId=102104108&durationDays=30&count=100&_=1598407761062",
    "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=A03&durationDays=30&count=100&_=1598407794216"
]

with requests.Session() as s:
    for url in urls:
        res = s.get(url)
    
        for i, item in enumerate(res.json(), 1):
            if i < 101:
                print(i, item["product_name"])
        print("*" * 30)
        