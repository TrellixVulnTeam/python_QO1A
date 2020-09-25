from bs4 import BeautifulSoup
import requests

with open("./beautifulsoup/story.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print(soup.find("a")) # find() : 첫번째만
print()
# 모든 a 태그 찾기
# find_all() : 필터 기준에 맞는 모든 태그 가져오기 (무조건 리스트 형태로 리턴)
print(soup.find_all("a"))
print(soup.find_all("a", limit=2))
