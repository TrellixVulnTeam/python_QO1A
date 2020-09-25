import requests
from lxml.html import fromstring

# lxml 문서 구조
# lxml.html
# lxml.etree

def main():
    url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1013"

    res = requests.get(url)
    parseData(res)

def parseData(res):
    # lxml 에서 파싱을 할 수 있는 구조로 변경
    root = fromstring(res.content)    # content는 byte로 가져옴
    print(type(root))   # <class 'lxml.html.HtmlElement'>

    channel = root.xpath("//channel")
    print(channel[0].tag)

    title = root.cssselect("title")    # cssselect는 list구조를 가져옴
    print("title", title[0].text_content())

    # 현재 문서의 모든 텍스트 출력
    # lxml.html에서만 가능
    print(root.text_content())

if __name__ == "__main__":
    main()
