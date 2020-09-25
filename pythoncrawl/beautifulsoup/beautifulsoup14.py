import requests
from bs4 import BeautifulSoup

# 클리앙 팁과 강좌 1~5페이지 타이틀 가져오기

for page_num in range(5):
    if page_num == 0:
        res = requests.get("https://www.clien.net/service/board/lecture")
    else:
        res = requests.get("https://www.clien.net/service/board/lecture?&od=T31&po="
        + str(page_num))

soup = BeautifulSoup(res.content, "html.parser")

# 타이틀 가져오기
titles = soup.select("div.list_title > a.list_subject > span.subject_fixed")
for title in titles:
    print(title.get_text().strip())
