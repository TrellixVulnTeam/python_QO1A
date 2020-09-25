# 네이버 / 다음 뉴스 가져오기
# 화면출력 / 파일 저장
import urllib.request as request
from urllib.error import URLError, HTTPError

target_url = [
    "https://newsis.com/view/?id=NISX20200824_0001139348&cID=10301&pID=10300",
    "https://news.v.daum.net/v/20200824070211318"
]

path_list = [
    "d:/download/navernews.html", "d:/download/daumnews.html"
]

for i, url in enumerate(target_url):
    try:
        response = request.urlopen(url)
        contents = response.read()
        print("-" * 50)
        print("header info - {} : {}".format(i, response.info()))
        print("Http status code - {}".format(response.getcode()))
        print("-" * 50)
        # 쌤 코딩 안됨 인코딩 안맞는듯
        # contents = request.urlopen(url).read().decode("euc-kr")
        # print(contents)
        with open(path_list[i], "wb") as f:
            f.write(contents)
    except HTTPError as e:
        print(e)
    else:
        print("저장성공")
