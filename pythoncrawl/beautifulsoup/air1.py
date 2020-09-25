import requests

serviceKey = "xi2PeqbCLzhL8NDeHy1uHD%2B%2BBQxcnfkvxjmp2YVtHkJFY4QxzlWFowPTqTLHZuBTD%2Fk%2BeZ7nmnH3MJBJCZJmYw%3D%3D"
stationName = "중랑구"
dataTerm = "DAILY"

url = ("http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey="
    + serviceKey
    + "&stationName="
    + stationName
    + "&dataTerm="
    + dataTerm
)

# param = {
#     "serviceKey" : "xi2PeqbCLzhL8NDeHy1uHD%2B%2BBQxcnfkvxjmp2YVtHkJFY4QxzlWFowPTqTLHZuBTD%2Fk%2BeZ7nmnH3MJBJCZJmYw%3D%3D",
#     "stationName" : "중랑구",
#     "dataTerm" : "DAILY"
# }

res = requests.get(url)
print(res.text)
