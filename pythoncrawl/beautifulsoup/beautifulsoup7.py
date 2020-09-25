# g마켓 카테고리 가져오기
import requests
from bs4 import BeautifulSoup

# g마켓 홈페이지 가져오기
res = requests.get("https://www.gmarket.co.kr/")
# 파싱하기
soup = BeautifulSoup(res.content, "html.parser")

# 카테고리 가져오기
cartegory = soup.find("span", {"class":"link__1depth-item"})
print("카테고리 : {}".format(cartegory.string))
print()

# 카테고리 리스트 가져오기
one_depth = soup.find_all("span", {"class":"link__1depth-item"})
for depth in one_depth:
    print(depth.string)
print()

# 카테고리 두번째
two_depth = soup.find_all("li", {"class":"list-item__2depth"})
for depth in two_depth:
    link1 = depth.find("a")["href"]   # 찾은 정보 안에서 링크 또 찾기
    print(link1, depth.string)
