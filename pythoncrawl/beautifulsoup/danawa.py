import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 로그인 시 보내는 formData
login_info = {
    "redirectUrl" : "http://www.danawa.com/",
    "loginMemberType" : "general",
    "id" : "hee12321",
    "isSaveId" : "true",
    "password" : "wogml123*"
}
headers = {
    "User-Agent" : UserAgent().chrome,
    "Referer" : "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F"
}
with requests.Session() as s:
    # 로그인 시도
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)

    # print(res.content.decode("utf-8"))

    # 로그인 성공 후 주문/배송 조회 페이지 요청
    res = s.get(
        "https://buyer.danawa.com/order/Order/orderList", headers=headers
    )
    # print(res.text)

    soup = BeautifulSoup(res.content, "html.parser")
    # 로그인 성공 체크
    check_id = soup.select_one("p.user")
    # print("id : {}".format(check_id))
    if check_id is None:
        raise Exception("Login 실패")

    # 사용자의 주문/배송정보 추출하기
    order_info = soup.select("div.sub_info > ul > li")
    # print(order_info)
    print("*** My Order Info ***")
    for item in order_info:
        name = item.find("span").string.strip()
        val = item.find("strong").string.strip()
        print("{} : {}".format(name, val))
