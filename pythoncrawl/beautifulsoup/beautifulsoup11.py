import requests
from bs4 import BeautifulSoup

res = requests.get("http://pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(res.content, "html.parser")

# Totally Normal Gifts 가져오기
title = soup.select_one("h1")
print("title : {}".format(title.string))
print()

# 첫번째 문단 가져오기(Here~~~)
paragraph1 = soup.find("div", id="content")
print("paragraph1 : {}".format(paragraph1))
print()

para1 = soup.select_one("div#content")
print("para1 : {}".format(para1))
print()

# 모든 img 태그 가져오기
img_all = soup.select("img")
print(img_all)
print()

# 테이블 내용 가져오기
table = soup.select("table", id="content")
print(table)

contents = soup.select("table#giftList")
for content in contents:
    print(content.get_text())
