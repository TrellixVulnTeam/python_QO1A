# urlopen() : 요청하는 url의 정보를 메모리에 올려서 분석할 때 사용
import urllib.request as req
from urllib.error import HTTPError
from urllib.parse import urlparse

encar_url = "http://www.encar.com/"

try:
    response = req.urlopen(encar_url)

    # 수신된 정보 확인
    print("type : {}".format(type(response)))
    print("geturl : {}".format(response.geturl()))
    print("status : {}".format(response.status))
    print("header : {}".format(response.getheaders()))
    print("getcode : {}".format(response.getcode()))
    print("parse : {}".format(urlparse("http://www.encar.com/"))

    contents = response.read().decode("EUC-KR")
except HTTPError as e:
    print(e)
else:
    # print("header info - {}".format(response.info()))
    print(contents[:4000])
