import json

data = """
    {
        "id":"01",
        "language":"python",
        "edition":"third",
        "author":"Heart",
        "history":[
            {
                "data":"2020-06-30",
                "item":"iPhone"
            },
            {
                "data":"2020-07-30",
                "item":"android"
            }
        ]
    }
"""

# json 형식의 데이터를 dict(딕셔너리) 형태로 변경
json_data = json.loads(data)

# print(json_data)
print(type(json_data))
print(json_data['id'])  # key값으로 value 출력
print(json_data['history'])
print(json_data['author'])
print(json_data['history'][0])
print(json_data['history'][1])
print(json_data['history'][0]['item'])
