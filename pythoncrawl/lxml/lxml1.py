# 크롤링(정보 수집)
# 웹에서 정보 가져오기(urllib, requests)
# 가져온 정보 중에서 유용한 내용 추출(파싱) - lxml  _조각내서 원하는 정보 뽑아내기
from lxml.html import tostring, fromstring
import requests

def main():
    url = "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=008&aid=0004460982&date=20200826&type=1&rankingSeq=5&rankingSectionId=105"
    res = requests.get(url)

    print("res.text : {}".format(type(res.text)))
    print("res content : {}".format(type(res.content)))
    
    # html 문서 구조 생성
    html_content = fromstring(res.text)  # html 형태로 만들어줘
    # print(html_content)
    data_extract(html_content)

def data_extract(html_content):
    # 신문기사 타이틀 출력
    # css 선택자 모두 가능
    title = html_content.cssselect("#articleTitle")
    print("title {}".format(type(title)))
    print("title {}".format(title[0].text_content))
    print("title {}".format(title[0].text))
    print("title {}".format(title[0].text))

    # 기사 속 이미지 가져오기
    images = html_content.cssselect(
        "#articleBodyContents > span:nth-child(23) > img"
    )
    for image in images:
        print(images.get("src"))
    
if __name__ == "__main__":
    main()
