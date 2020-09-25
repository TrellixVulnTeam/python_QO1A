import requests
from lxml.html import fromstring, tostring

def main():
    res = requests.get("https://www.naver.com")
    # 신문사 링크 리스트 얻기
    urls = scrape_news_list_page(res)

    # 링크 리스트 파일 저장하기
    for name, url in urls.items():
        with open("d:/download/link1.txt", "a") as f:
            f.write(name + ":" + url + "\n")

def scrape_news_list_page(res):
    # 파싱 구조로 변경
    root = fromstring(res.content)

    urls = {}   # dict형태로 urls 생성 / "key" : "value"
    
    for a in root.xpath("//*[@class='thumb_area']/div[@class='thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid']"):
        name, url = extract_contents(a)
        urls[name] = url
    return urls

def extract_contents(a):
    # 추출한 영역에서 다시 추출 가능
    # 신문사 주소 추출
    link = a.xpath("./div[@class='popup_wrap']/a[3]")
    link = link[0].get("href")      # cssselect는 1개라도 list로 반환
    
    # 회사명 추출
    name = a.xpath("./a/img")[0].get("alt")    
    print(name, link)
    return name, link

if __name__ == "__main__":
    main()
