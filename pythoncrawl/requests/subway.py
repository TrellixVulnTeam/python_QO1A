import requests

def info():   # 모듈화_다른 클래스에서 호출해 쓸 수 있도록
    # wiki_url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
    wiki_url = "https://ko.wikipedia.org/wiki/서울_지하철"

    res = requests.get(wiki_url)
    # print(res.text)
    print(res.content)  # byte type으롤 데이터 받아올 때


if __name__ == "__main__":
    info()
    