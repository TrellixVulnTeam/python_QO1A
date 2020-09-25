# dict
# key, value 형태
# 순서 없음, 중복 안됨, 수정,삭제 가능
# 자바의 map
#%%
# key : value 형태로 작성
# key 값은 정수형, 문자형 가능
dict1 = {"name": "Park", "age": 12}
print(dict1)

dict2 = {0: "Hello", 1: "Python", 2: "Coding"}
print(dict2)

dict3 = {"arr": [1, 2, 3, 4, 5]}
print(dict3)

dict4 = {"arr": (1, 2, 3, 4, 5)}
print(dict4)

#%%
# dict에서 특정 키의 값 출력하기
# get() : 없는 키 값일 떄 None로 돌려줌
print(dict1["name"])
# print(dict1["addr"])  # KeyError

print(dict1.get("addr"))    # None

#%%
# dict에 내용 추가하기
dict1["birth"] = "1115"
print(dict1)

dict2[3] = [4,5,6]
print(dict2)

dict4["test"] = (8, 9, 10)
print(dict4)

#%%
# dict에 내용 삭제하기
del dict1["birth"]
print(dict1)

#%%
# dict key값 가져오기
print(dict1.keys())
print(dict2.keys())
print(dict3.keys())
print(dict4.keys())

#%%
# dict value값 가져오기
print(dict1.values())
print(dict2.values())
print(dict3.values())
print(dict4.values())

#%%
# key, value 형태로 가져오기
print(dict1.items())
print(dict2.items())
print(dict3.items())
print(dict4.items())

#%%
# 해당 키가 딕셔너리 안에 있는지 확인
print("name" in dict1)
print(5 in dict2)

#%%
# dict 안의 모든 값 지우기
dict1.clear()
print(dict1)   # {}  => dict 자체를 지우는게 아니라 안의 값을 지움

#%%
# dict 출력 => 원하는 모양대로 출력
myInfo = {"name":"kim","age":24,"city":"seoul"}
for k in myInfo.keys():
    print(k, end=" ")
print()
for v in myInfo.values():
    print(v, end=" ")
print()
for k,v in myInfo.items():
    print(k,v)

#%%
# 4 계절을 대표하는 과일을 dict 구조로 생성
# {"봄":"딸기,..."}
fruits = {"봄":"딸기", "여름":"수박","가을":"감","겨울":"귤"}

# 가을의 과일이 무엇인지 출력하기
print(fruits["가을"])
# 쌤 코딩
for k in fruits.keys():
    if k == "가을":
        print(fruits[k])
for k,v in fruits.items():
    if k == "가을":
        print(v)

# 사과가 포함되었는지 확인하기
if fruits.values() == "사과":
    print("사과가 포함되어 있습니다")
else:
    print("사과가 없습니다")
# 쌤 코딩
for v in fruits.values():
    if v == "사과":
        print("사과가 포함됨")
        break
else:
    print("사과가 포함되지 않음")

#%%
# comprehension
fruit = {f for f in fruits.values()}
print(fruit)

fruit = {f for f in fruits.values() if f!="사과"}
print(fruit)

fruit = { (k,v) for (k,v) in fruits.items()}
print(fruit)
