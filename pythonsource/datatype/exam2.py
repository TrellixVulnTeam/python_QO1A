#%%
# A : 90, B : 80, C : 70 의 형태를 dict 구조로 생성한 후 key : value 형태로 출력한다.
dict1 = {"A":90,"B":80,"C":70}
print(dict1)

#%%
# 위의 dict에서 B 키에 해당하는 값만 출력한다.
print(dict1.keys())

for k in dict1.keys():
    print(k, end=" ")

print()
# 쌤 코딩
print(dict1["B"])

#%%
# B 키 값을 삭제한 후 전체 dict를 출력한다
dict1["B"]=""
print(dict1)

print()
# 쌤 코딩
del dict1["B"]
print(dict1)

#%%
# 다음 항목을 dict로 생성하기
# 성인 - 10000, 청소년 - 7000, 아동 - 3000
dict2 = {"성인":10000,"청소년":7000,"아동":3000}
print(dict2)

#%%
# 위에서 선언한 dict에 소아 - 0 항목 추가한 후 출력하기
dict2["소아"] = 0
print(dict2)

#%%
# 위에서 선언한 dict의 key 값만 출력하기
print(dict2.keys())

for k in dict2.keys():
    print(k, end=" ")

#%%
# 위에서 선언한 dict의 value 값만 출력하기
print(dict2.values())

for v in dict2.values():
    print(v, end=" ")

#%%
# foods라는 딕셔너리를 생성하고 각 음식에 맞는 value를 출력하기
# foods = {
#    "떡볶이":"순대",
#    "짜장면":"탕수육",
#    "라면":"삼각김밥",
#    "피자":"스파게티",
#    "양꼬치":"칭따오",
#    "치킨":"치킨볼",
#    "삼겹살":"상추"
# }

foods = {
   "떡볶이":"순대",
   "짜장면":"탕수육",
   "라면":"삼각김밥",
   "피자":"스파게티",
   "양꼬치":"칭따오",
   "치킨":"치킨볼",
   "삼겹살":"상추"
}
print(foods)

# 사용자에게 좋아하는 음식을 고르게 한 후 그 음식과 궁합이 맞는 음식 출력하기(반복문 사용)
# 내 코딩
# food = input("좋아하는 음식을 입력해주세요")
# while "끝":
#     if food.keys() == food:
#         for v in foods.values():
#             print(v)
#     else:
#         "다시 입력해주세요"

# 쌤 코딩
while True:
    food = input(str(list(foods.keys())) + " 중 좋아하는 것은?")
    if food in foods:
        print("%s 궁합 음식은 %s 입니다." % (food, foods[food]))
    elif food == "끝":
        break
    else:
        print("다른 음식을 선택해 주세요")

# 입력값이 '끝'이라는 글자가 들어오면 반목문을 종료
# 키 값이 없는 음식을 고르면 "다른 음식을 선택해 주세요" 출력하기
