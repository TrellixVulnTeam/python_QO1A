import requests
from bs4 import BeautifulSoup
import os
import urllib.request as req

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum"
param = {"query": "트럭"}

res = requests.get(url, params=param)

# 이미지 저장 경로
savePath = "d:/download/"

# 폴더 생성
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    print("폴더 생성 실패", e.filename)
    raise RuntimeError("System Exit")
else:
    print("폴더 생성")

# 이미지 태그 찾기
soup = BeautifulSoup(res.content, "html.parser")

img_list = soup.select("div.img_area a.thumb._thumb img")
print(img_list)

for i, img in enumerate(img_list, 1):
    # 저장 파일명 및 경로
    fullfileName = os.path.join(savePath, savePath + str(i) + ".png")

    # 다운로드 요청
    req.urlretrieve(img["data-source"], fullfileName)

