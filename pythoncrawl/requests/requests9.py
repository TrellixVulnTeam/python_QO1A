import requests

with requests.Session() as s:
    res = s.get("https://jsonplaceholder.typicode.com/users", stream=True)
    # print("json : {}".format(res.json()))  # 전체 데이터 확인용
    for person in res.json():
        for k, v in person.items():
            print("{} : {}".format(k, v))
        print()

