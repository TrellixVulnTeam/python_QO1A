import requests
from bs4 import BeautifulSoup

# 요청가져오기
url = "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=008&aid=0004462568&date=20200828&type=1&rankingSeq=1&rankingSectionId=101"
res = requests.get(url)

# BeautyfulSoup 객체 생성 (파싱할 문서 구조, 파싱을 무엇으로 할건지)
soup = BeautifulSoup(res.content, "html.parser")

# soup 객체를 이용해 파싱하기
# find() : 검색되는 제일 첫번째 리턴
title = soup.find("h3", id="articleTitle")
print(title)
print(title.string)
print(title.get_text())
