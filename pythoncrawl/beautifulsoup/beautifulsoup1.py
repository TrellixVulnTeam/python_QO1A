# BeautifulSoup : 크롤링 유명 패키지
# 사용하기 쉽고, cssselector, xpath 이용해서 파싱 가능

# 단계
# 요청 가져오기
# BeautyfulSoup 객체 생성
# soup 객체를 이용해 파싱하기
import requests
from bs4 import BeautifulSoup

# 요청가져오기
url = "https://ko.wikipedia.org/wiki/서울_지하철"
res = requests.get(url)

# BeautyfulSoup 객체 생성 (파싱할 문서 구조, 파싱을 무엇으로 할건지)
soup = BeautifulSoup(res.text, "html.parser")  # html.parser : 파싱도구 기본
# print(soup)
print(type(soup))   # <class 'bs4.BeautifulSoup'>
print(soup.prettify())

# soup 객체를 이용해 파싱하기
print("head", soup.head)
print()
print("title", soup.title)
print()
# string or get.text() 둘 중에 하나 되는거 사용
print("title 문자열", soup.title.string)
print("title 문자열", soup.title.get_text())
