import urllib.request as request    # urllib.request 라이브러리 전체 데리고 오기
from urllib.error import URLError, HTTPError   # urllib.error 에서 일부만 데리고 오기

target_url = [
    "https://www.naver.com",
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F011%2F2019%2F01%2F04%2F0003478759_001_20190104080006672.jpg&type=sc960_832"
]

# 파일 저장 경로
path_list = [
    "d:/download/naver.html", "d:/download/jenny.jpg"
]

# for i, url in target_url:
for i, url in enumerate(target_url):
    try:
        # 정보 가져오기
        response = request.urlopen(url)
        # 정보 읽기
        contents = response.read()
        # 상태 정보 확인
        print("-" * 50)
        print("header info - {} : {}".format(i, response.info()))
        print("Http status code - {}".format(response.getcode()))
        print("-" * 50)
        print()
        # 파일 저장(w : write, b : byte)  // text형태가 아닌 다른 형태를 저장할때는 b 줘야 함!
        with open(path_list[i], "wb") as f:
            f.write(contents)

    except HTTPError as e1:
        print(e1)
    except URLError as e2:
        print(e2)
    else:
        print("성공~")
