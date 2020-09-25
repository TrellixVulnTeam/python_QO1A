import requests
from lxml import etree

# lxml 문서 구조
# lxml.html
# lxml.etree

def main():
    url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001"

    res = requests.get(url)
    parseData(res)

def parseData(res):
    # lxml 에서 파싱을 할 수 있는 구조로 변경
    root = etree.fromstring(res.content)    # content는 byte로 가져옴
    # print(type(root))   # <class 'lxml.etree._Element'>

    print(root)       # <Element rss at 0x267d5514b00>
    print(root.tag)   # rss 

    children = root[0]
    print("children tag : {}".format(children.tag))

    for child in children:
        print(child.tag, ":", child.text)
        for ch in child:
            print(ch.tag, ":", ch.text)

if __name__ == "__main__":
    main()
