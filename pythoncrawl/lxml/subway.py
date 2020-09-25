import requests
from lxml.html import fromstring, tostring

def info():   # 모듈화_다른 클래스에서 호출해 쓸 수 있도록
    # wiki_url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
    wiki_url = "https://ko.wikipedia.org/wiki/서울_지하철"

    res = requests.get(wiki_url)
    # print(res.text)
    # print(res.content)  # byte type

    # 파싱을 할 수 있는 구조 생성
    data = fromstring(res.text)

    # url에서 원하는 img의 xPath copy해왔을 때
    # //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/td/a/img
    # // : 문서 처음부터 다 찾고
    # * : 앞에 아무거나 와도되고
    # id="mw-content-text" : id가 mw-content-text 인거 찾아오고
    # 그 뒤로는 태그 순서

    # img 태그 찾기
    # for a in data.xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[1]/td/a/img"):
    #     print(tostring(a))   # string 형태로 출력해줘
    #     print()
    #     print(a.xpath("@src"))   # src 값만 가져오기

    # css select
    for a in data.cssselect("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"):
        print(tostring(a))   # string 형태로 출력해줘
        print()
        print(a.get("src"))   # src 값만 가져오기
        
if __name__ == "__main__":
    info()
    