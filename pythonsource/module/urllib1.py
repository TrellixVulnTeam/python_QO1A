# urllib : URL을 다루는 모듈(라이브러리)
from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)
